from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print(rank)

# MPI.SUM sums it up on all processes and gives the result to process 0
total_sum = comm.reduce(rank, op=MPI.SUM, root=0)

if rank == 0:
    print(f"The sum of all ranks is: {total_sum}")