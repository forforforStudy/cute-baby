use std::process::Command;
use crate::GLOBAL_ENVIRONMENT;

pub trait Executor {
    fn run(&self, command: String) -> ();
}

pub struct LocalADBExecutor {}

impl LocalADBExecutor {
    pub fn new() -> LocalADBExecutor {
        LocalADBExecutor {}
    }
}

impl Executor for LocalADBExecutor {
    fn run(&self, command: String) -> () {
        let adb_exe_file = &GLOBAL_ENVIRONMENT.adb_exe_file;

        match adb_exe_file.to_str() {
            None => {
                panic!("adb.exe 文件未找到")
            }
            Some(adb_exe_file_str) => {
                let command_str = command.as_str();
                let mut child = Command::new(adb_exe_file_str)
                    .args([command_str])
                    .spawn()
                    .expect(format!("指令执行失败: \"{}\"", command).as_str());

                let execute_result = child.wait().expect(format!("执行指令过程中发生错误: \"{}\"", command).as_str());

                println!("指令\"{}\"运行结束, Success = {}", command_str, execute_result.success());
            }
        }
    }
}