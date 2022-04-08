#![cfg_attr(
all(not(debug_assertions), target_os = "windows"),
windows_subsystem = "windows"
)]

pub mod flask_web;

use flask_web::screencaps_client::{get_screencaps_list, control_screencaps_running, clean_all_screencaps};

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![get_screencaps_list, control_screencaps_running, clean_all_screencaps])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}

