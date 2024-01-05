# Prerequisite Research

## Einstein Summation
- How does Einstein Summation work? What are all the ways expressions can be simpified? How are they evaluated?

### Types of components
These different component types will be defined with objects

## More advanced notation


## Variables and components
### Parital Derivatives

To simplify equations, the partial derivative symbol is simplified to $\partial_{\mu}$, which means:
$$\partial_\mu = \frac{\partial}{\partial \mu}$$
And simply means you take the partial derivative of the thing to the right of it with respect to the index.

### Kronecker Delta $\delta_{ij}$
The Kronecker Delta, in most simple terms, is a value which is 1 when $i$ and $j$ have the same value, otherwise they are 0. In un-defined, four dimenional matrix form, the Kronecker Delta is defined as:

$$\delta_{ij} = \begin{bmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

And acts as any other 4x4 dimensional indexed vector


### Christoffel Symbols ${\Gamma_\mu}^{\alpha\beta}$

Christoffel symbols are used a lot in General Relativity, and represent the connection coefficients that indicate how coordinate systems change from one point to another in curved spacetime.

They are defeined as the following:

$${\Gamma^\lambda}_{\mu\nu} = \frac{1}{2}g^{\lambda\alpha} \left(\partial_\mu g_{\alpha\nu} + \partial_\nu g_{\alpha\mu} - \delta_\alpha g_{\mu\nu} \right )$$

