
<p align="center"><strong> Name: Abdelaziz Salah  | Code 9202810</strong></p>

#  Defragmentation of Heap Algorithms
## First Fit
* Definition:
  * This method keeps the free/busy list of jobs organized by memory location, low-ordered to high-ordered memory. In this method, first job claims the first available memory with space more than or equal to it’s size.
* When to Use:
  * When the performance is your main concern as it is very fast in processing and execution. 
  * When you want to minimize memory fragmentation.
  * But on the other hand it wastes a lot of memory, so it has poor memory utilization. 

## Next Fit
* Definition:
  * It is a modified version of `First Fit` algorithm. 
  *  It begins as the first fit to find a free partition but when called next time it starts searching from where it left off, not from the beginning.
  * This helps in, to avoid the usage of memory always from the head (beginning) of the free blockchain. 
* When to Use: 
  * It solves one of the major problems of the `First Fit` algorithms which is the internal fragmentation problem by avoiding allocation always from the beginning, but it starts from the end of the last allocation.
  * so we can use it instead of the `First fit` if we care about memory managment. 
## Best Fit
* Definition: 
  *  a memory allocation technique used in operating systems to allocate memory to a process.
  *  the operating system searches through the list of free blocks of memory to find the block that is closest in size to the memory request from the process. Once a suitable block is found, the operating system splits the block into two parts: the portion that will be allocated to the process, and the remaining free block.
* When to Use: 
  * When we want to achieve the best memory utilization.
  * and when we want to minimize the memory fragmentation as it tends to allocate smaller blocks of memory that are less likely to become fragmented. 
  * But on the other hand it has a worst performance compared to FF and NF algorithms. 

## Worst Fit
* Definition: 
  *  the process traverses the whole memory and always search for the largest hole/partition, and then the process is placed in that hole/partition. It is a slow process because it has to traverse the entire memory to search the largest hole. 
* When to Use:
  * Since this process chooses the largest hole/partition, therefore there will be large internal fragmentation. Now, this internal fragmentation will be quite big so that other small processes can also be placed in that leftover partition. 
  * also it may be useful if all the existing processes tends to be of the same size. 
  * In that case, if you have a large free block (say 50MB) and most of the processes submitted tend to be smaller than that (say 10MB), it would actually be better to put them in this big block so that you can use the leftover space better, rather than put them in a barely bigger block (maybe 11-15MB) which would leave some small unusable space.

## Quick Fit
* Definition: 
  * The Quick Fit algorithm is a memory allocation strategy used in operating systems to assign memory to processes. It is a variation of the first-fit algorithm that aims to minimize memory fragmentation.

  *   In Quick Fit, the memory is divided into several fixed-size partitions or blocks, each of which can accommodate a process of a specific size. These partitions are pre-allocated and stored in a list or array. When a new process arrives, the algorithm searches for the smallest partition that can accommodate the process and assigns it to that partition.
* When to use:
  * It  can be useful in situations where there is a high demand for memory allocation and deallocation, and the size of the processes being allocated is relatively fixed. This makes it suitable for real-time systems or systems with a large number of short-lived processes, such as web servers.
  * Also can also be useful in situations where the memory requirements of a process are known in advance, as the fixed-size partitions can be pre-allocated to optimize memory utilization.
  * But it is not the best choice if the size of the processes is highly variable. 
  * as It can lead to significant memory fragmentation. 

 
 
<p align="center"><strong>Delivered to DR/ Basem Ibrahem</strong></p>
