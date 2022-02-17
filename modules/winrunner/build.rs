extern crate fs_extra;

use std::env::{current_dir, var};
use std::path::Path;
use fs_extra::dir::{CopyOptions, copy};

fn main() {
    match current_dir().unwrap().to_str() {
        None => {}
        Some(dir_str) => {
            /*
                拷贝 resources 文件到 target 目录下
             */
            let resource_dir = Path::new(dir_str).join("resources");
            let copy_options = CopyOptions::new();

            println!("build: resource_dir = {}", resource_dir.to_str().unwrap());

            match var("OUT_DIR") {
                Ok(out_dir) => {
                    println!("build: out_dir = {}", out_dir);
                    match copy(resource_dir, Path::new(&out_dir), &copy_options) {
                        Ok(_) => {
                            println!("build: resources 拷贝完成")
                        }
                        Err(_) => {
                            println!("build: 拷贝 resources 失败， 跳过")
                        }
                    };
                }
                Err(_) => {
                    panic!("build: 找不到输出目录")
                }
            };
        }
    };
}