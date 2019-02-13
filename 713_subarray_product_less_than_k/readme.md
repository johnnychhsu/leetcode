## 713. Subarray product less than k
Use a sliding window concept, each time multiply one item to the current product. If it is less than k, then add all subarray that contains the newest element. If larger or equal than k, then divide the rightest element till the current product less than k. <br />
