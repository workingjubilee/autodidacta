// using "as" recklessly can lead to surprising results
fn main() {
    let x: i32 = -1;
    println!("x as i32: {}", x);
    println!("x as u8: {}", x as u8);
    println!("x as u8 as char: {}", x as u8 as char);
}