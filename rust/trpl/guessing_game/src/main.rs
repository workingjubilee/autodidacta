use std::io::{stdin};
use std::cmp::Ordering::{Less, Greater, Equal};
use rand::{Rng, thread_rng};

fn main() {
    println!("Guess the number!");

    let secret_number = thread_rng().gen_range(1, 101);
    println!("Please input your guess.");

    loop {
        let mut guess = String::new();
        stdin().read_line(&mut guess).expect("No read?");
        if let Ok(guess) = guess.trim().parse::<u32>() {
            println!("You guessed: {}", guess);

            match guess.cmp(&secret_number) {
                Less => println!("Too small!"),
                Greater => println!("Too big!"),
                Equal => { println!("You win!"); break; }
            }
        } else {
            continue;
        }
    }
}
