use rxing::{DecodeHints, helpers::*};
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];
    let try_harder: bool = &args[2] == "true";
    let mut hints = DecodeHints::default().with(rxing::DecodeHintValue::TryHarder(try_harder));
    let binding = detect_in_file_with_hints(
        filename,
        Some(rxing::BarcodeFormat::DATA_MATRIX),
        &mut hints,
    );
    let result: String;
    //.expect("Reading datamatrix: ");
    if let Ok(text) = binding {
        result = text.getText().to_owned();
    } else {
        result = binding.expect_err("Error: ").to_string();
    }
    println!("Result: {result}");
}
