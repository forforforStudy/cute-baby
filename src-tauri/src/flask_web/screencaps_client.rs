use reqwest;

const SCREENCAPS_HOST: &str = "http://localhost:5555";

#[tauri::command]
pub fn screencaps_client_box() -> String {

    let result = reqwest::blocking::get(format!("{}/v0.1/screencaps", SCREENCAPS_HOST))
        .unwrap()
        .text();

    match result {
        Ok(screencaps) => {
            screencaps
        }
        Err(reason) => {
            "reason".to_string()
        }
    }
}