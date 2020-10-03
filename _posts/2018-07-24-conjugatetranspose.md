---
layout: article
title: "Conjugate Transpose"
tags:
  - Math
permalink: conjugate_transpose.html
---

## Introducing the Conjugate Transpose
In linear algebra, one of the first things one does is to transpose matrices. For the most part, one first learns linear algebra by using matrices such that they belong to the field of real numbers ($$\mathbb{R}$$). However it is possible for the elements of the matrix to exist in the complex field $$\mathbb{C}$$. So if given a matrix $$A$$

$$A \in \mathbb{R} \longrightarrow A \in \mathbb{C}$$

When dealing with a matrix that exists in the complex field $$\mathbb{C}$$, transposing the matrix is not as trivial, where it needs to in fact go through a conjugate transpose. The conjugate transpose of the matrix $$A$$ may be shown as

$$A^* \text{ or } A^H \text{ or } A^\dagger$$

The $$A^\dagger$$ is often used in quantum mechanics and it's pronounced as "A dagger". It's defined as

$$A^H = (\overline{A})^T = \overline{A^T}$$

Therefore, as an example, given the matrix $$A$$,

$$A = \begin{bmatrix} 1 & 3+i \\ 4-2i & 2i \end{bmatrix}$$

$$A^H = \begin{bmatrix} 1 & 4-2i \\ 3-i & -2i \end{bmatrix}$$

But why is it that we need to take the conjugate of the transpose?

## Derivation

Complex numbers can be shown as $$2\times 2$$ matrices,

$$a+bi \equiv \begin{bmatrix} a & -b \\ b & a \end{bmatrix}$$

By the same principle of a **rotation matrix**,

$$R = \begin{bmatrix} \cos(\theta) & -\sin(\theta) \\ \sin(\theta) & \cos(\theta) \end{bmatrix}$$

if we were to assume that

$$\begin{cases}
a = r \cos(\theta) \\
b = r \sin(\theta) \\
r = 1
\end{cases}$$

Then we are inherently able to say that

$$R = \begin{bmatrix} a & -b \\ b & a \end{bmatrix}$$

Therefore, since each complex number is a $$2\times 2$$ submatrix, by substituting it, the matrix $$A \in \mathbb{C}^{m\times n}$$ becomes $$A \in \mathbb{C}^{2m\times 2n}$$, and when taking the transpose, the conjugate is also needed to be taken.

## General Example

Given $$A \in \mathbb{C}^{2\times 2}$$,

$$\begin{align}
A &= \begin{bmatrix} \color{blue}{a+bi} & \color{red}{c+di} \\ \color{pink}{e+fi} & \color{cyan}{g+hi} \end{bmatrix} \\
&= \begin{bmatrix}
\color{blue}{a} & \color{blue}{-b} & \color{red}{c} & \color{red}{-d} \\
\color{blue}{b} & \color{blue}{a} & \color{red}{d} & \color{red}{c} \\
\color{pink}{e} & \color{pink}{-f} & \color{cyan}{g} & \color{cyan}{-h} \\
\color{pink}{f} & \color{pink}{e} &  \color{cyan}{h} & \color{cyan}{g}
\end{bmatrix} \end{align}$$

$$\begin{align}
A^T
&= \begin{bmatrix}
\color{blue}{a} & \color{blue}{b} & \color{pink}{e} & \color{pink}{f} \\
\color{blue}{-b} & \color{blue}{a} & \color{pink}{-f} & \color{pink}{e} \\
\color{red}{c} & \color{red}{d} & \color{cyan}{g} & \color{cyan}{h} \\
\color{red}{-d} & \color{red}{c} &  \color{cyan}{-h} & \color{cyan}{g}
\end{bmatrix} \\
&= \begin{bmatrix} \color{blue}{a-bi} & \color{pink}{e-fi} \\ \color{red}{c-di} & \color{cyan}{g-hi} \end{bmatrix} = A^H
\end{align}$$

So, as shown above, because the transpose of the full $$A$$ matrix (i.e. where the complex numbers are substituted by their respective $$2\times 2$$ matrices), one can see that by definition, it yields the **conjugate transpose** of a matrix $$A$$, such that $$A\in \mathbb{C}$$. Therefore, in reality, the same way that every time we do a simple scalar multiplication, we are in fact doing a dot product but in one-dimension, every time we do a transpose of a matrix, we are in fact doing a conjugate transpose.
