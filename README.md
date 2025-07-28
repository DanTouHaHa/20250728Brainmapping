Pipeline for Generating Brain Surface Mapping Files
This repository contains the pipeline and resources for generating .curv brain mapping files for cortical surface visualization using FreeSurfer.

Contents
Data_input_for_creating_curv_mapping_file.xlsx
main_function.m
fwrite3.m
write_curv.m
Fig_2a_left.curv, 
Fig_2a_right.curv, 
Fig_2b_left.curv, 
Fig_2b_middle.curv, 
Fig_2b_right.curv
Fig_S5a.curv, 
Fig_S5b.curv


1️⃣ Environment
Server: XXX (please specify your server model)
Operating System: XXXX
Software Dependencies:
MATLAB 2018b
FreeSurfer v7.1.1
Freeview (FreeSurfer visualization tool)

2️⃣ Generate .curv Files
2.1 Input
Data_input_for_creating_curv_mapping_file.xlsx: Source values to be mapped onto cortical surfaces.
2.2 Code Files
main_function.m: Main script for generating .curv files.
fwrite3.m: Helper function for binary writing.
write_curv.m: Writes data to FreeSurfer .curv format.

3️⃣ Visualization Using Freeview (e.g., for Figure 2a & 2b) 需要图
3.1 Figure 2a (Right Three Panels)
Open Freeview
File → Load Surface → rh.pial_semi_inflated
Overlay → Load Generic → Fig_2a_right.curv
Overlay → Configure
Adjust colorbar
Choose Right view, Inferior view, Left view as needed

3.2 Figure 2b (Right Two Panels)
File → Load Surface → rh.pial_semi_inflated
Overlay → Load Generic → Fig_2b_right.curv
Overlay → Configure
Adjust colorbar
Choose Right view, Inferior view

4️⃣ Output: .curv Files
4.1 Figure 2a
Left panel: Fig_2a_left.curv
Right panels: Fig_2a_right.curv

4.2 Figure 2b
Left panel: Fig_2b_left.curv
Middle panel: Fig_2b_middle.curv
Right two panels: Fig_2b_right.curv

4.3 Supplementary Figure 5
Left panel: Fig_S5a.curv
Right panel: Fig_S5b.curv

Notes
Ensure hemisphere (lh or rh) and inflated surface (pial_semi_inflated) match the mapping files.



