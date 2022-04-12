#![cfg_attr(
all(not(debug_assertions), target_os = "windows"),
windows_subsystem = "windows"
)]

pub mod flask_web;

use flask_web::screencaps_client::{get_screencaps_list, control_screencaps_running, clean_all_screencaps};
use flask_web::server_bootstrap::boostrap_py_web;

fn main() {
    // 启动python web服务
    boostrap_py_web();

    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![get_screencaps_list, control_screencaps_running, clean_all_screencaps])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}

