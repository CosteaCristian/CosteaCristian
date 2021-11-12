//965396

//Toma Costea Cristian

//Coursework 2 

import java.util.ArrayList;
public class ModuleCatalog {
	
    //
  
	 public static final int ARRAYLENGT = 1000;
	
    public static final int MAX_LVL = 6;
	
	
    public static final int MAX_COD = 999;
	
	public static final int FIRST_COD = 100;
    
	
	public static final int FIRST_LVL = 3;
    //
    private ArrayList<Module> moduleList = new ArrayList<Module>();
    private boolean[] codeStat = new boolean[ARRAYLENGT];

//use of levels, dept codes and dept names
    public void addModule(int lvl, int cod, String name, String dptCod){
        if (lvl >= FIRST_LVL && lvl <= MAX_LVL && cod >= FIRST_COD && cod <= MAX_COD
                && (dptCode.equals("RO") || dptCode.equals("GE")) && !codeStat[cod]) {
            Module curr = new Module(lvl, cod, name, dptCod);
            moduleList.add(curr);
            codeStat[code]=true;
        }
    }
//

 public ArrayList<Module> getModulesByLevel(int lvl){
        ArrayList<Module> levelList = new ArrayList<Module>();
        for (int i=0; i<moduleList.size(); i++){
            if (moduleList.get(i).getLevel()==lvl){
                levelList.add(moduleList.get(i));
            }
        }
        return levelList;
    }

//

   public  ArrayList<Module> getAllModules(){

        return moduleList;
    }

//




public String formatCatalogList(ArrayList<Module> list){
        String formList="";
        for (int i=0; i < list.size(); i++) {
            formaList += list.get(i).getDepartment()+":" + list.get(i).getLevel() + "-"
                    + list.get(i).getModuleCode() + " " + list.get(i).getModuleName()
                    + " (" + list.get(i).getDepartmentName() + ")\n";
        }
        return formList;
    }

//


 public ArrayList<Module> getModulesByDeptCode(String deptCode){
        ArrayList<Module> dptList = new ArrayList<Module>();
        for (int i=0; i<moduleList.size(); i++){
            if (moduleList.get(i).getDepartment().equals(deptCode)){
                dptList.add(moduleList.get(i));
            }
        }
        return dptList;
    }
//


    public String formatCatalogList(ArrayList<Module> list){
        String formList="";
        for (int i=0; i < list.size(); i++) {
            formaList += list.get(i).getDepartment()+":" + list.get(i).getLevel() + "-"
                    + list.get(i).getModuleCode() + " " + list.get(i).getModuleName()
                    + " (" + list.get(i).getDepartmentName() + ")\n";
        }
        return formList;
    }
}
