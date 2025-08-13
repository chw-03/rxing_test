use rxing::{DecodeHints, helpers::*};

fn main() {
    let mut hints = DecodeHints::default().with(rxing::DecodeHintValue::TryHarder(true));
    let binding = detect_in_file_with_hints(
        "frame.png",
        Some(rxing::BarcodeFormat::DATA_MATRIX),
        &mut hints,
    );
    //.expect("Reading datamatrix: ");
    if let Ok(text) = binding {
        let result = text.getText().to_owned();
        println!("Result: {result}");
    } //else {
        //result = binding.expect_err("Error: ").to_string();
    //}
    //println!("Result: {result}");
}
