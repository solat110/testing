{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Age batao 25\n",
      "counter se ticket lo\n",
      " Andar jao \n"
     ]
    }
   ],
   "source": [
    "print (\"content-type: text/html\")\n",
    "#Age Restrition\n",
    "age = int(input ('Age batao '))\n",
    "\n",
    "if age >= 20:\n",
    "    print(\"counter se ticket lo\")\n",
    "  \n",
    "    if age != 20 : \n",
    "          print(' Andar jao ')\n",
    "        \n",
    "else:\n",
    "    print('Bary hokar anna ')\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your Age3.2\n",
      "Your Child is Eligible for Pre-Nursury Class\n"
     ]
    }
   ],
   "source": [
    "#Age vise Admission Open\n",
    "age = float(input (\"Enter your Age\"))\n",
    "\n",
    "if age > 2.0 and age < 3.5:\n",
    "    print (\"Your Child is Eligible for Pre-Nursury Class\")\n",
    "else:\n",
    "    print('Sorry Your Child is not allow for Admission in Pre-Nursury')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 <= 7\n",
      "2 <= 7\n",
      "3 <= 7\n",
      "4 <= 7\n",
      "5 <= 7\n",
      "6 > 5\n",
      "7 > 5\n",
      "8 > 5\n",
      "9 > 5\n",
      "10 > 5\n",
      "11 > 5\n",
      "12 > 5\n",
      "13 > 5\n",
      "14 > 5\n",
      "15 > 5\n",
      "16 > 5\n",
      "17 > 5\n",
      "18 > 5\n",
      "19 > 5\n",
      "20 > 5\n"
     ]
    }
   ],
   "source": [
    "a = 0\n",
    "while a < 20:\n",
    "    a = a + 1\n",
    "    if a > 5:\n",
    "        print (a,\">\",5)\n",
    "    elif a <= 7:\n",
    "        print (a,\"<=\",7)\n",
    "    else:\n",
    "        print (\"Neither test was true\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
