#![cfg_attr(feature = "const", feature(const_fn, const_vec_new))]

mod adb;
mod environment;

use environment::{GLOBAL_ENVIRONMENT};
use crate::adb::execute::{Executor, LocalADBExecutor};

fn main() {
    println!("Hello, world!");

    let executor = LocalADBExecutor::new();

    executor.run(String::from("start-server"));

    executor.run(String::from("devices"));
}
