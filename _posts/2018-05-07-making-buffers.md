---
layout: page
title: "Making Buffers Using the Henderson-Hasselbach Equation"
categories:
  - Instructions
  - Chemistry & Biochemistry
---

One is able to use the Henderson-Hasselbach equation in order to approximate the desired pH prior to trying to set the pH using the pH meter. This way, one is arguably able to utilize much less reagents for the making of buffers.
Given the Henderson-Hasselbach equation,  

$$ \text{pH} = \text{p}K_a + \log \left( \frac{[BASE]}{[ACID]} \right) $$  

$$ \text{pH} = \text{p}K_a + \log \left( \frac{[A^-]}{[HA]} \right) $$

We can reduce it to
$$ 10^{\text{pH} - \text{p}K_a} = \frac{[A^-]}{[HA]}$$

So, if we'd like to make a  **$$0.1\text{M}$$ phosphate buffer ($$\text{pH } 8.00$$)** using sodium phosphate dibasic anhydrous ($$\text{Na}_2\text{HPO}_4$$) as the base, and sodium phosphate monobasic ($$\text{NaH}_2\text{PO}_4$$) as our acid, with a $$\text{pH} = 8.00$$, knowing that the $$\text{p}K_a = 7.20$$, we say that

$$ \frac{[A^-]}{[HA]} = 10^{\text{pH} - \text{p}K_a} = 10^{8.00-7.20} = \frac{6.3096}{1}$$

This allows us to say that

$$\begin{cases}
\% \text{ Base} = \frac{6.3096}{1+6.3096} = 86.319 \% \text{ Na}_2\text{HPO}_4\\
\% \text{ Acid} = \frac{1}{1 + 6.3096} = 13.681 \% \text{ NaH}_2\text{PO}_4
\end{cases} $$

Then we can calculate the molarities:

$$\begin{cases}
\text{Base Molarity } = \text{strength} \times \% = (0.01 \text{M}) \times (86.319 \%) = 8.6319 \text{mM} \text{ Na}_2\text{HPO}_4\\
\text{Acid Molarity } = \text{strength} \times \% = (0.01 \text{M}) \times (13.681 \%) = 1.3681 \text{mM} \text{ NaH}_2\text{PO}_4
\end{cases}$$

Therefore, to make a $$\text{100 ml}$$ solution, we'd need

$$ \begin{cases}
\text{Base grams } = (8.6319 \times 10^{-3} \text{M})(0.10 \text{L})(141.96 \frac{g \text{ Na}_2\text{HPO}_4 }{mol}) = 0.1225 g \text{ Na}_2\text{HPO}_4 \\
\text{Acid grams } = (1.3618 \times 10^{-3} \text{M})(0.10 \text{L})(137.99 \frac{g \text{ NaH}_2\text{PO}_4 }{mol}) = 0.0188 g \text{ NaH}_2\text{PO}_4
\end{cases} $$

And that's it! *Note that the this method approximates the pH desired, however doesn't guarantee a perfect pH, but at that point, all that is needed is some NaOH or HCl in order to calibrate the solution*
