use std::env;
use std::path::{Path, PathBuf};
use std::process::Command;

pub fn boostrap_py_web() {
    let mut path_buf_result = env::current_dir();

    match path_buf_result {
        Ok(mut path_buf) => {
            path_buf.push(&Path::new("../src-py/main.py"));

            match path_buf.to_str() {
                None => {}
                Some(path_str) => {
                    println!("运行Python上的Web服务");
                    Command::new("cmd").args(["/C", format!("python {}", path_str).as_str()]).spawn();
                }
            }
        }
        Err(_) => {}
    }
}