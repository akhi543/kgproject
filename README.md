# About the project:
Genome sequencing is a process of identifying the order of bases - adenine (A), cytosine (C), guanine (G), and thymine (T) in a particular Deoxyribonucleic acid (DNA). This task is performed in multiple stages and various tools are involved for the same. Two examples of tools are fastqc and trimmomatic. To carry out this task, a user interacts with the system in terms of running the scripts, observing and analyzing the logs of the scripts, specifying suitable parameters for the tools, etc. The goal of this project is capture all the user behaviour for this pipeline of task and store it in digital format. This information can then be used to gain insights in to the process and reduce research overhead for future, similar tasks. For example, if we identify that a particular tool runs well with “xGB” of memory and “yGB” of virtual memory, and we capture and store that detail, we can use it in future for performing similar task. The task of capturing the information and retrieving it later on is done using knowledge graph, which is a highly efficient and popular data storage and retrieval mechanism in today’s world. Also, for querying the knowledge graph, I am using Stardog studio which is a dedicated software solution for graph databases.

# Running instructions:
    
## Generating knowledge triples

python3 scriptsAndLogsParser.py
    This will generate the triples file (scriptsLogs.ttl)

## Loading triples and querying them

1. Install and configure stardog (https://www.stardog.com/docs)
    a. wget https://downloads.stardog.com/stardog/stardog-latest.zip && unzip stardog-latest.zip
    b. mv -R stardog-<version> /opt/
    c. put these in .bashrc
        export STARDOG_HOME="/var/stardog" 
        export PATH="$PATH:/opt/stardog-7.4.4/bin"
2. Start stardog: `stardog-admin server start`
3. Download stardog studio (https://www.stardog.com/studio/)
4. Load database (ttl file created above) into stardog and run queries over it. 
