import sys

class SecurityLog:
    def __init__(self,path):
        self.filepath=path
        self.total_lines = 0
        self.valid_lines = 0
        self.malformed_lines =0 
        self.analysis_completed = False
        self.severity_counts = {}
    
    def _parse_line(self,fileline):
        #normalises the file before checking for basic integrity of each line
        line=fileline.strip().lower().split()
        if len(line)>=3 :
            date,time,severity = line[:3]
            if "-" in date and ":" in time and severity.isalpha():
                return severity
            else :
                return None
        else:
            return None
        
    def analyse(self):
        # For Reset purposes incase anyone runs this function twice
        self.total_lines = 0
        self.valid_lines = 0
        self.malformed_lines =0 
        self.analysis_completed = False
        self.severity_counts = {}

        #To catch errors with file
        try:
            with open (self.filepath , "r") as file:
                for line in file:
                    self.total_lines+=1
                    severity = self._parse_line(line)
                    if severity :
                        self.valid_lines+=1
                        self._update_counts(severity)
                    else:
                        self.malformed_lines+=1

                self.analysis_completed = True
        except FileNotFoundError :
            sys.exit("File Doesnt Exist")
        except PermissionError :
            sys.exit("Permission Denied")

        
    
    def _update_counts(self,severity):
        #increases count of existing severity or creates new with default count as 1
        if severity in self.severity_counts:
            self.severity_counts[severity]+=1           
        else:
            self.severity_counts[severity]= 1 

    def report(self) :
        #prints summary report of file once analysis is done
        if not self.analysis_completed :
            print("Analysis not completed. Please run analyse() first.")
            return 
    
        print("\n===== Log Summary =====")
        print("\nTotal lines : " ,self.total_lines)
        print("Valid entries : " ,self.valid_lines)
        print("Malformed lines : ", self.malformed_lines)

        if self.valid_lines == 0:
            print("No valid log entries found.")
            
        else:
            print("\nSeverity Counts:")
            # sorts based on values of keys for most number high priority (Gives Tuple form )
            sorted_count = sorted(self.severity_counts.items(), key = lambda value : value[1], reverse=True) 
            for severity ,count in sorted_count : #(assigns the value part to count fromt the tuple)
                print(f"{severity.upper():<12} : {count}")                



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python log_analyzer.py <filename>")
    else:
        filename = sys.argv[1]
        log = SecurityLog(filename)
        log.analyse()
        log.report()
