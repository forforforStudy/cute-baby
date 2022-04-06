use reqwest;
use serde::{Serialize, Deserialize};

const SCREENCAPS_HOST: &str = "http://localhost:5555";

#[derive(Serialize, Deserialize)]
pub struct ScreencapsList {
    items: Vec<String>,
    total: u32,
}

#[tauri::command]
pub fn screencaps_client_box() -> ScreencapsList {
    let result = reqwest::blocking::get(format!("{}/v0.1/screencaps", SCREENCAPS_HOST))
        .unwrap()
        .json::<ScreencapsList>();

    match result {
        Ok(screencaps) => {
            screencaps
        }
        Err(_reason) => {
            ScreencapsList {
                items: vec![],
                total: 0,
            }
        }
    }
}