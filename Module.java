public class Module {
   //
    private String mdlName;
    private int lvl;
    private String dptCode;
    private int modulCode;
    private String dptName;
   //
    public Module(int lvlCurr, int modCodeCurr, String modNameCurr, String dptCodeCurr) {
        lvl = lvlCurr;
        modulCode = modCodeCurr;
        dptCode = deptCodeCurr;
        mdlName = modNameCurr;
        detDeptName();

    }


    public void detDeptName() {
        if (dptCode.equals("RO")
            dptName = "Romanian Language";

        } else if (dptCode.equals("GE")) {
            dptName = "German Language";
        }
    }


    public String getDepartment(){
        return dptCode;
    }
    public int getLevel(){
        return lvl;

    
    }


    public String getModuleName(){
        return mdlName;

    
    }
	 public String getDepartmentName(){
        return dptName;
    

    }


    public int getModuleCode(){
        return modulCode;
    }
}


