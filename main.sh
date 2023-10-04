#!/bin/bash

if [ $# -ne 2 ]; then
  echo "Usage: $0 <number1> <number2>"
  exit 1

else    
    echo "Arg 1 $1"
    echo "Arg 2 $2"
    echo "Total length of Args ${#}"
    echo $(bc <<< "$1 + $2")
fi

if [[ "$2" =~ [^0-9] ]]; then
    echo "Variable is a string"

elif [ -v variable ]; then
    echo "Varibale is a array"

else 
    echo "Variable is a integer"
fi

