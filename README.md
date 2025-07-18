# 🥤 Vending Machine: Learning About **Return Values** in Functions!

## 📚 What is a **return** in a function?

Imagine you walk up to a vending machine. You put some money in, press a button, and the machine *gives you back* a snack.

A function in code works in a similar way — you give it something (like money 💰), and it gives you something back (like a snack 🍫). That “something” it gives back is called the **return value**.

---

## 🔧 Example: A Vending Machine Function

Here’s our vending machine in code:

```csharp
string vendingmachine(int cash)
{
    if (cash == 1000)
    {
        return "milkshake";
    }
    else if (cash == 500)
    {
        return "chocolate bar";
    }
    else
    {
        return "no snack available";
    }
}

string snack = vendingmachine(1000);
Console.WriteLine(snack); // Output: milkshake
```

### 🧠 What's Happening?

* We call the function like this: `vendingmachine(1000)`
* We gave it 1000 shillings.
* The function checked: "Hmm, is that 1000? Yes!" So it returned `"milkshake"`.
* The returned value `"milkshake"` was saved in the variable `snack`.
* Then we printed it using `Console.WriteLine(snack);`

---

## 🤔 Why use `return`?

A function’s `return` lets us:

* **Get a result** from the function.
* **Use that result** somewhere else in the program.

Without `return`, it’s like putting money in a vending machine… and nothing comes out! 😱

---

## 🧪 Practice Time! Try these:

### 1. 🍕 Add More Snacks

Add more choices to the vending machine. Example:

* 2000 = "pizza slice"
* 100 = "chewing gum"

```csharp
// Add these in your function using more "else if" statements
```

---

### 2. 📱 Make a Phone Store!

Write a function called `buyPhone` that takes money and returns the phone name.

```csharp
string buyPhone(int cash)
{
    if (cash == 20000)
    {
        return "Samsung Galaxy A14";
    }
    else if (cash == 50000)
    {
        return "iPhone SE";
    }
    else
    {
        return "Not enough money";
    }
}
```

Try calling:

```csharp
string phone = buyPhone(50000);
Console.WriteLine(phone);
```

---

### 3. 🏫 School Store

Create a function called `buySchoolItem(int cash)` with these options:

* 50 = "pen"
* 100 = "exercise book"
* 200 = "math set"

Let the student call the function with different amounts of money.

---

## 🧼 Quick Tip: One Return Per Turn

Once a `return` runs in a function, the function stops immediately. So only one snack comes out per visit!

---


