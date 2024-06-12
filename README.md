# SnakeRL_22b3313
SoC 2024 project in which I build a automated Snake Game using PyGame and implement it using RL

## SnakeRL, Assignment -1.

### Problem Statement:

![image](https://github.com/lvl0goblin/SnakeRL_22b3313/assets/172357113/bd58ef70-e4ed-46e2-81fb-f81f538ae93f)

What I understood about Markov Chains is that my “my actions in the future are decided by my actions in the present, regardless of the past”.

$$
P(X_{t+1} = x_{t+1} | X_t = x_t, X_{t-1} = x_{t-1}, \ldots, X_0 = x_0) = P(X_{t+1} = x_{t+1} | X_t = x_t)
$$


  So for the above problem what I do is I first get the transition matrix from the user which will be manually given. Then ask for the starting point ,time and the ending point. It I to be noted that the nodes are represented by the row numbers in the transition matrix so the user has to give the starting and ending nodes’ identity in terms of its corresponding row number.
  Say M is our matrix I will calculate M raised to the power T (time). Then I  create the starting vector , multiply it with this matrix and get the probablity for reaching the ending state.
 
