use std::env::current_dir;
use std::path::Path;
use once_cell::sync::Lazy;

#[derive(Debug)]
pub struct Environment {
    pub resource_dir: Box<Path>,
    pub adb_dir: Box<Path>,
    pub adb_exe_file: Box<Path>
}

impl Environment {
    pub fn new () -> Environment {
        let adb_exe_name = "adb.exe";
        let current_dir_path = match current_dir() {
            Ok(x) => x,
            Err(_) => panic!("Environment 初始化失败"),
        };

        let resource_dir_path = current_dir_path.join("resources");
        let adb_dir_path = resource_dir_path.join("adb-platform-tools");

        Self {
            resource_dir: Box::from(resource_dir_path.as_path()),
            adb_dir: Box::from(adb_dir_path.as_path()),
            adb_exe_file: Box::from(adb_dir_path.join(adb_exe_name).as_path())
        }
    }
}

pub static GLOBAL_ENVIRONMENT: Lazy<Environment> = Lazy::new(|| {
    Environment::new()
});