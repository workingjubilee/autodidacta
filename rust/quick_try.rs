use std::error::Error;
use std::fs::File;

// Returning this boxed Error with Result allows quickly hacking something.
fn main() -> Result<(), Box<dyn Error>> {
    File::open("hello.txt")?;
    Ok(())
}
