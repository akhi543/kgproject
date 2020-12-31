import sys, re, os

ttlFile = open('abc.ttl', 'w')

def rawQCScriptParser(file):
    filepath = file
    file = file.replace('/', '_')
    ttlFile.write("## RawQCScriptFile triples\n")
    ttlFile.write(":{} rdf:type :RawQCScriptFile .\n".format(file))
    with open(filepath, "r") as f:
        for line in f:
            walltime = re.findall('walltime=(.*)', line)
            if len(walltime) > 0:
                ttlFile.write(":{} :walltime \"{}\" .\n".format(file, walltime[0]))
            nodes = re.findall('nodes=(\d+)', line)
            if len(nodes) > 0:
                ttlFile.write(":{} :nodes \"{}\" .\n".format(file, nodes[0]))
            ppn = re.findall('ppn=(\d+)', line)
            if len(ppn) > 0:
                ttlFile.write(":{} :ppn \"{}\" .\n".format(file, ppn[0]))
            fastqcparams = re.findall('fastqc (.*)', line)
            for param in fastqcparams:
                ttlFile.write(":{} :fastqcParam :{} .\n".format(file, param))
    ttlFile.write("\n")
    ttlFile.write("\n")
    
def trimQCScriptParser(file):
    ttlFile.write("## TrimQCScriptFile triples\n")
    ttlFile.write(":{} rdf:type :TrimQCScriptFile .\n".format(file))
    with open(file, "r") as f:
        for line in f:
            walltime = re.findall('walltime=(.*)', line)
            if len(walltime) > 0:
                ttlFile.write(":{} :walltime \"{}\" .\n".format(file, walltime[0]))
            nodes = re.findall('nodes=(\d+)', line)
            if len(nodes) > 0:
                ttlFile.write(":{} :nodes \"{}\" .\n".format(file, nodes[0]))
            ppn = re.findall('ppn=(\d+)', line)
            if len(ppn) > 0:
                ttlFile.write(":{} :ppn \"{}\" .\n".format(file, ppn[0]))
            fastqcparams = re.findall('fastqc (.*)', line)
            for param in fastqcparams:
                ttlFile.write(":{} :fastqcParam :{} .\n".format(file, param))
    ttlFile.write("\n")
    ttlFile.write("\n")
    
def trimScriptParser(file):
    ttlFile.write("## TrimScriptFile triples\n")
    ttlFile.write(":{} rdf:type :TrimScriptFile .\n".format(file))
    with open(file, "r") as f:
        for line in f:
            walltime = re.findall('walltime=(.*)', line)
            if len(walltime) > 0:
                ttlFile.write(":{} :walltime \"{}\" .\n".format(file, walltime[0]))
            nodes = re.findall('nodes=(\d+)', line)
            if len(nodes) > 0:
                ttlFile.write(":{} :nodes \"{}\" .\n".format(file, nodes[0]))
            ppn = re.findall('ppn=(\d+)', line)
            if len(ppn) > 0:
                ttlFile.write(":{} :ppn \"{}\" .\n".format(file, ppn[0]))
            fastqcparams = re.findall('fastqc (.*)', line)
            
    ttlFile.write("\n")
    ttlFile.write("\n")

def rawQCLogParser(file):
    filepath = file
    file = file.replace('/', '_')
    ttlFile.write("## RawQCLogFile triples\n")
    ttlFile.write(":{} rdf:type :RawQCLogFile .\n".format(file))
    with open(filepath, "r") as f:
        for line in f:
            dataFile = re.findall('Analysis complete for (.*)', line)
            if len(dataFile) > 0:
                ttlFile.write(":{} :AnalysisResult :complete .\n".format(dataFile[0]))
            walltime = re.findall('walltime=(.*)', line)
            if len(walltime) > 0:
                ttlFile.write(":{} :walltime \"{}\" .\n".format(file, walltime[0]))
            nodes = re.findall('nodes=(\d+)', line)
            if len(nodes) > 0:
                ttlFile.write(":{} :nodes \"{}\" .\n".format(file, nodes[0]))
            ppn = re.findall('ppn=(\d+)', line)
            if len(ppn) > 0:
                ttlFile.write(":{} :ppn \"{}\" .\n".format(file, ppn[0]))
            cput = re.findall('cput=(.*)', line)
            if len(cput) > 0:
                ttlFile.write(":{} :cput \"{}\" .\n".format(file, cput[0]))
            mem = re.findall('^mem=(.*)', line)
            if len(mem) > 0:
                ttlFile.write(":{} :mem \"{}\" .\n".format(file, mem[0]))
            vmem = re.findall('vmem=(.*)', line)
            if len(vmem) > 0:
                ttlFile.write(":{} :vmem \"{}\" .\n".format(file, vmem[0]))
    ttlFile.write("\n")
    ttlFile.write("\n")
    
def trimQCLogParser(file):
    ttlFile.write("## TrimQCLogFile triples\n")
    ttlFile.write(":{} rdf:type :TrimQCLogFile .\n".format(file))
    with open(file, "r") as f:
        for line in f:
            dataFile = re.findall('Analysis complete for (.*)', line)
            if len(dataFile) > 0:
                ttlFile.write(":{} :AnalysisResult :complete .\n".format(dataFile[0]))
            walltime = re.findall('walltime=(.*)', line)
            if len(walltime) > 0:
                ttlFile.write(":{} :walltime \"{}\" .\n".format(file, walltime[0]))
            nodes = re.findall('nodes=(\d+)', line)
            if len(nodes) > 0:
                ttlFile.write(":{} :nodes \"{}\" .\n".format(file, nodes[0]))
            ppn = re.findall('ppn=(\d+)', line)
            if len(ppn) > 0:
                ttlFile.write(":{} :ppn \"{}\" .\n".format(file, ppn[0]))
            cput = re.findall('cput=(.*)', line)
            if len(cput) > 0:
                ttlFile.write(":{} :cput \"{}\" .\n".format(file, cput[0]))
            mem = re.findall('^mem=(.*)', line)
            if len(mem) > 0:
                ttlFile.write(":{} :mem \"{}\" .\n".format(file, mem[0]))
            vmem = re.findall('vmem=(.*)', line)
            if len(vmem) > 0:
                ttlFile.write(":{} :vmem \"{}\" .\n".format(file, vmem[0]))
    ttlFile.write("\n")
    ttlFile.write("\n")

def trimLogParser(file):
    pass
        


def main():

    # print(os.getcwd())

    scriptsAndLogsDir = 'scriptsAndLogs/ScriptsLogsOutputs'
    os.chdir(os.path.join(os.getcwd(), scriptsAndLogsDir))

    
    rawQCScriptDir = 'RawQCScript'
    trimQCScriptDir = 'TrimQCScripts'
    trimScriptDir = 'TrimScripts'
    rawQCLogDir = 'RawQCLog'
    trimQCLogDir = 'TrimQCLogs'
    trimLogDir = 'TrimLogs'

    rawQCScripts = os.listdir(rawQCScriptDir)
    trimQCScripts = os.listdir(trimQCScriptDir)
    trimScripts = os.listdir(trimScriptDir)
    rawQCLogs = os.listdir(rawQCLogDir)
    trimQCLogs = os.listdir(trimQCLogDir)
    trimLogs = os.listdir(trimLogDir)

    ttlFile.write("PREFIX : <http://example.org/>\n")
    ttlFile.write("\n\n")

    for x in rawQCScripts:
        rawQCScriptParser(os.path.join(rawQCScriptDir, x))

    for x in rawQCLogs:
        rawQCLogParser(os.path.join(rawQCLogDir, x))

    # for x in trimQCScripts:
    #     trimQCScriptParser(os.path.join(trimQCScriptDir, x))

    # for x in trimQCLogs:
    #     trimQCLogParser(os.path.join(trimQCLogDir, x))

    # for x in trimScripts:
    #     trimScriptParser(os.path.join(trimScriptDir, x))

    # for x in trimLogs:
    #     trimLogParser(os.path.join(trimLogDir, x))



if __name__ == '__main__':
    main()