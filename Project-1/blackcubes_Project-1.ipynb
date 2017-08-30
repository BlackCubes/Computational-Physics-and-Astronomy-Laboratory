{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#This is an attempt for the problem 1.a\n",
    "\n",
    "import sympy\n",
    "\n",
    "sympy.init_printing()\n",
    "\n",
    "m, k, x_0, v_0, omega_0, t = sympy.symbols('m, k, x_0, v_0, omega_0, t')\n",
    "x = sympy.Function('x')\n",
    "\n",
    "sol = sympy.dsolve(sympy.Derivative(x(t), t, 2) + omega_0 * x(t))\n",
    "\n",
    "ics = [sympy.Eq(sol.args[1].subs(t, 0), x_0), sympy.Eq(sol.args[1].diff(t).subs(t, 0), 0)]\n",
    "\n",
    "solved_ics = sympy.solve(ics)\n",
    "\n",
    "full_sol = sol.subs(solved_ics[0])\n",
    "full_sol"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#This is for my attempt on problem 1.c, but did not work so well...\n",
    "\n",
    "from numpy import zeros, linspace\n",
    "import numpy as np\n",
    "from matplotlib import pyplot as plt\n",
    "\n",
    "U_0 = 1\n",
    "\n",
    "def osc_2nd_order(U_0, omega, dt, T):\n",
    "    dt = float(dt)\n",
    "    Nt = int(round(T/dt))\n",
    "    u = zeros(Nt+1)\n",
    "    t = linspace(0, Nt*dt, Nt+1)\n",
    "    \n",
    "    u[0] = U_0\n",
    "    u[1] = u[0] - 0.5*dt**2*omega**2*u[0]\n",
    "    for n in range(1, Nt):\n",
    "        u[n+1] = 2*u[n] - u[n-1] - dt**2*omega**2*u[n]\n",
    "    return u, t"
   ]
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
   "version": "3.6.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
