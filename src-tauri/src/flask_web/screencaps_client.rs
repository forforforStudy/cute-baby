use reqwest;
use reqwest::blocking::RequestBuilder;
use serde::{Serialize, Deserialize};

const SCREENCAPS_HOST: &str = "http://localhost:5555";

#[derive(Serialize, Deserialize)]
pub struct ScreencapsList {
    items: Vec<String>,
    total: u32,
}

#[tauri::command]
pub fn get_screencaps_list() -> ScreencapsList {
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

#[tauri::command]
pub fn control_screencaps_running(start: bool) -> u8 {
    let client = reqwest::blocking::Client::new();
    let request_url = match start {
        true => format!("{}/v0.1/screencaps/start", SCREENCAPS_HOST),
        false => format!("{}/v0.1/screencaps/stop", SCREENCAPS_HOST)
    };

    match client.post(request_url).send() {
        Ok(result) => {
            1
        }
        Err(_) => {
            0
        }
    }
}

#[tauri::command]
pub fn clean_all_screencaps() -> u8 {
    let client = reqwest::blocking::Client::new();

    match client.post(format!("{}/v0.1/screencaps/clean", SCREENCAPS_HOST)).send() {
        Ok(_result) => {
            1
        }
        Err(_) => {
            0
        }
    }
}