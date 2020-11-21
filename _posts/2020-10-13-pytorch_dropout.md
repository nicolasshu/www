

```python
# %%
drop = nn.Dropout()
x = torch.ones(1,10)
# %%
drop.train()
drop(x)

# %%
drop.eval()
drop(x)

```