#![cfg_attr(
  all(not(debug_assertions), target_os = "windows"),
  windows_subsystem = "windows"
)]

pub mod flask_web;

use flask_web::screencaps_client::screencaps_client_box;

fn main() {
  tauri::Builder::default()
    .invoke_handler(tauri::generate_handler![screencaps_client_box])
    .run(tauri::generate_context!())
    .expect("error while running tauri application");
}

