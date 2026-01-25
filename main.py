#!/usr/bin/env python3
"""
Project: My Awesome Project
Created by: Vikas Coding Editor Social
Description: A sample Python application with multiple features
"""

import os
import sys
from datetime import datetime

def display_welcome():
    """Display welcome message"""
    print("=" * 50)
    print("MY AWESOME PROJECT")
    print("=" * 50)
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

def get_user_input():
    """Get input from user"""
    print("Please enter your information:")
    print("-" * 30)
    
    name = input("Your name: ").strip()
    age = input("Your age: ").strip()
    
    return name, age

def process_data(name, age):
    """Process user data"""
    print("\n" + "=" * 50)
    print("PROCESSING YOUR DATA...")
    print("=" * 50)
    
    results = {
        'name': name,
        'age': age,
        'name_length': len(name) if name else 0,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    return results

def display_results(results):
    """Display processed results"""
    print("\n📊 RESULTS:")
    print("-" * 30)
    
    for key, value in results.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    
    print("\n" + "=" * 50)
    print("Thank you for using this application!")
    print("Created with ❤️ by Vikas Coding Editor Social")
    print("=" * 50)

def main():
    """Main function"""
    display_welcome()
    
    name, age = get_user_input()
    
    if not name:
        print("\n⚠️  No name provided. Using 'Guest' as default.")
        name = "Guest"
    
    results = process_data(name, age)
    display_results(results)
    
    # Save to file
    try:
        with open('user_data.txt', 'a') as f:
            f.write(f"{results['timestamp']} - Name: {name}, Age: {age}\n")
        print("\n✅ Data saved to 'user_data.txt'")
    except Exception as e:
        print(f"\n❌ Error saving file: {e}")

if __name__ == "__main__":
    main()