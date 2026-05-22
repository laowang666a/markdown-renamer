from core import scan_directory,generate_new_name,build_rename_jobs,resolve_conflicts

from schemas import RenameJob

def test_scan_directory_invalid(tmp_path):
    fake_path = tmp_path / "nonexistent"
    assert scan_directory(fake_path) == []
def test_scan_directory(tmp_path):
    assert scan_directory(tmp_path) == []
    # assert scan_directory("wrong/path") == []
    test_md1 = tmp_path / "hello1.md"
    test_txt1 = tmp_path / "hello2.txt"
    test_md1.touch()
    test_txt1.touch()
    assert scan_directory(tmp_path) == [test_md1]
    test_md2 = tmp_path / "hello.md"
    test_md2.touch()
    assert set(scan_directory(tmp_path)) == {test_md1,test_md2}

def test_generate_new_name(tmp_path):
    test_md = tmp_path / "hello.md"
    test_md.touch()
    assert generate_new_name(test_md, "%Y-%m-%d") == "2026-05-19.md"

def test_build_rename_jobs(tmp_path):
    test_md1 = tmp_path / "hello1.md"
    test_txt1 = tmp_path / "hello2.txt"
    test_md2 = tmp_path / "hello.md"
    test_md1.touch()
    test_txt1.touch()
    test_md2.touch()
    output = build_rename_jobs(tmp_path,"%Y-%m-%d")
    assert len(output) == 2
    assert RenameJob(test_md1,"2026-05-19.md") in output
    assert RenameJob(test_md2, "2026-05-19.md") in output

def test_resolve_conflicts(tmp_path):
    test_md1 = tmp_path / "hello1.md"
    test_txt1 = tmp_path / "hello2.txt"
    test_md2 = tmp_path / "hello.md"
    test_md1.touch()
    test_txt1.touch()
    test_md2.touch()
    Rename_list = build_rename_jobs(tmp_path, "%Y-%m-%d")
    final_output = resolve_conflicts(Rename_list)
    assert len(final_output) == 2
    expected_job1 = RenameJob(file_path=test_md1, new_name="2026-05-19_2.md", status="pending")
    expected_job2 = RenameJob(file_path=test_md2, new_name="2026-05-19.md", status="pending")

    # 3. 使用 in 断言（无视列表顺序影响）
    assert expected_job1 in final_output
    assert expected_job2 in final_output




