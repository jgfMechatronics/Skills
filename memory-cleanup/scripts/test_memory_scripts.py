"""Tests for dump_blocks.py and restore_blocks.py"""
import pytest
import requests
from unittest.mock import MagicMock, patch

from dump_blocks import dump, fetch_blocks, write_blocks
from restore_blocks import patch_block, read_blocks, restore


# ---------------------------------------------------------------------------
# Shared test data
# ---------------------------------------------------------------------------

AGENT_ID = "agent-test-123"
SERVER_URL = "http://localhost:8283"

SAMPLE_BLOCKS = [
    {"label": "persona", "value": "I am Sonnet.", "id": "block-1"},
    {"label": "human", "value": "James is the user.", "id": "block-2"},
]


def make_mock_response(json_data, status_code=200):
    mock = MagicMock()
    mock.status_code = status_code
    mock.json.return_value = json_data
    mock.raise_for_status.return_value = None
    return mock


def make_error_response():
    mock = MagicMock()
    mock.raise_for_status.side_effect = requests.HTTPError("500 Server Error")
    return mock


# ---------------------------------------------------------------------------
# dump_blocks tests
# ---------------------------------------------------------------------------


class TestFetchBlocks:
    def test_requests_correct_url(self):
        with patch("requests.get") as mock_get:
            mock_get.return_value = make_mock_response(SAMPLE_BLOCKS)
            fetch_blocks(SERVER_URL, AGENT_ID)
            mock_get.assert_called_once()
            url = mock_get.call_args.args[0]
            assert url == f"{SERVER_URL}/v1/agents/{AGENT_ID}/core-memory/blocks"

    def test_returns_block_list(self):
        with patch("requests.get") as mock_get:
            mock_get.return_value = make_mock_response(SAMPLE_BLOCKS)
            result = fetch_blocks(SERVER_URL, AGENT_ID)
            assert result == SAMPLE_BLOCKS

    def test_raises_on_http_error(self):
        with patch("requests.get") as mock_get:
            mock_get.return_value = make_error_response()
            with pytest.raises(requests.HTTPError):
                fetch_blocks(SERVER_URL, AGENT_ID)


class TestWriteBlocks:
    @pytest.fixture(autouse=True)
    def setup(self, tmp_path):
        self.output_dir = tmp_path / "dump"
        write_blocks(SAMPLE_BLOCKS, str(self.output_dir))

    def test_creates_output_dir(self):
        assert self.output_dir.exists()

    def test_creates_backup_dir(self):
        assert (self.output_dir / "Backup").exists()

    def test_writes_each_block(self):
        for block in SAMPLE_BLOCKS:
            assert (self.output_dir / f"{block['label']}.txt").read_text() == block["value"]

    def test_backup_matches_primary(self):
        for block in SAMPLE_BLOCKS:
            primary = (self.output_dir / f"{block['label']}.txt").read_text()
            backup = (self.output_dir / "Backup" / f"{block['label']}.txt").read_text()
            assert primary == backup


class TestDump:
    """Integration tests: mock fetch_blocks (HTTP boundary), let write_blocks run real."""

    @pytest.fixture(autouse=True)
    def setup(self, tmp_path):
        self.output_dir = tmp_path / "dump"
        patcher = patch("dump_blocks.fetch_blocks", return_value=SAMPLE_BLOCKS)
        self.mock_fetch = patcher.start()
        yield
        patcher.stop()

    def test_creates_files_for_each_block(self):
        dump(SERVER_URL, AGENT_ID, str(self.output_dir))
        for block in SAMPLE_BLOCKS:
            assert (self.output_dir / f"{block['label']}.txt").read_text() == block["value"]

    def test_prints_block_count(self, capsys):
        dump(SERVER_URL, AGENT_ID, str(self.output_dir))
        assert "2" in capsys.readouterr().out


# ---------------------------------------------------------------------------
# restore_blocks tests
# ---------------------------------------------------------------------------


class TestReadBlocks:
    def test_reads_txt_files(self, tmp_path):
        (tmp_path / "persona.txt").write_text("I am Sonnet.")
        (tmp_path / "human.txt").write_text("James is the user.")
        result = dict(read_blocks(str(tmp_path)))
        assert result["persona"] == "I am Sonnet."
        assert result["human"] == "James is the user."

    def test_skips_non_txt_files(self, tmp_path):
        (tmp_path / "persona.txt").write_text("I am Sonnet.")
        (tmp_path / "README.md").write_text("Not a block.")
        result = dict(read_blocks(str(tmp_path)))
        assert set(result.keys()) == {"persona"}

    def test_skips_backup_subdir(self, tmp_path):
        backup_dir = tmp_path / "Backup"
        backup_dir.mkdir()
        (backup_dir / "persona.txt").write_text("backup copy")
        (tmp_path / "persona.txt").write_text("real copy")
        result = dict(read_blocks(str(tmp_path)))
        assert result["persona"] == "real copy"
        assert len(result) == 1

    def test_label_from_filename(self, tmp_path):
        (tmp_path / "operational.txt").write_text("ops notes")
        labels = [label for label, _ in read_blocks(str(tmp_path))]
        assert labels == ["operational"]


class TestPatchBlock:
    def test_patches_correct_url(self):
        with patch("requests.patch") as mock_patch:
            mock_patch.return_value = make_mock_response({})
            patch_block(SERVER_URL, AGENT_ID, "persona", "new content")
            mock_patch.assert_called_once()
            url = mock_patch.call_args.args[0]
            assert url == f"{SERVER_URL}/v1/agents/{AGENT_ID}/core-memory/blocks/persona"

    def test_sends_value_in_body(self):
        with patch("requests.patch") as mock_patch:
            mock_patch.return_value = make_mock_response({})
            patch_block(SERVER_URL, AGENT_ID, "persona", "new content")
            assert mock_patch.call_args.kwargs.get("json") == {"value": "new content"}

    def test_raises_on_http_error(self):
        with patch("requests.patch") as mock_patch:
            mock_patch.return_value = make_error_response()
            with pytest.raises(requests.HTTPError):
                patch_block(SERVER_URL, AGENT_ID, "persona", "new content")


class TestRestore:
    """Integration tests: mock patch_block (HTTP boundary), let read_blocks run real."""

    @pytest.fixture(autouse=True)
    def setup(self, tmp_path):
        self.tmp_path = tmp_path
        (tmp_path / "persona.txt").write_text("I am Sonnet.")
        (tmp_path / "human.txt").write_text("James is the user.")

    def test_patches_all_blocks(self):
        with patch("restore_blocks.patch_block") as mock_patch:
            restore(SERVER_URL, AGENT_ID, str(self.tmp_path))
        calls = {c.args[2]: c.args[3] for c in mock_patch.call_args_list}
        assert calls == {"persona": "I am Sonnet.", "human": "James is the user."}

    def test_prints_progress(self, capsys):
        with patch("restore_blocks.patch_block"):
            restore(SERVER_URL, AGENT_ID, str(self.tmp_path))
        out = capsys.readouterr().out
        assert "persona" in out
        assert "human" in out
