## 857. Minimum cost to hire k workers
### Priority Queue
The idea is to sort the wage/quality, then select k worker in this array according to its ratio. Each time collect k workers, we calculate the total wage.
<br />
Because there are minimum requirement for each worker, we first calculate the ratio `wage/quality` for each worker. The requirement asks that the paid worker should receive the wage according to the quality ratio in the paid list.
<br />
Thus, once we have k worker, we use the newest worker's minimum cost as an unit for the current ratio. Thus we can get the total cost. The reason we can use `current quality sum * newest unit cost` is that, they should be paid according to the ratio of their quality. So the ratio of the highest worker can be used to calculate the total cost.
