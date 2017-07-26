use std::io;

fn main()
{
    let mut a = String::new();
    let mut b = String::new();
    io::stdin().read_line(&mut a).ok();
    io::stdin().read_line(&mut b).ok();

    println!("{}", a.trim().parse::<i64>().unwrap() - b.trim().parse::<i64>().unwrap());
}
