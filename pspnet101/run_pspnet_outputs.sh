#PBS -l walltime=08:00:00
#PBS -lselect=1:ncpus=4:mem=24gb:ngpus=1:gpu_type=P100
#PBS -J 1-13
module load anaconda3/personal
source activate tensorflowgpu
cd $PBS_O_WORKDIR
cd pspnet101
pwd
python pspnet102.py $PBS_ARRAY_INDEX