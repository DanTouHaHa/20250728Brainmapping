from nibabel.freesurfer.io import read_morph_data
import numpy as np
import pandas as pd

# 替换为你自己的文件路径
curv_path = 'Inattention_rh.curv'

# 读取数据
curv_data = read_morph_data(curv_path)

# 找出所有非0的顶点索引和值
non_zero_mask = ~np.isclose(curv_data, 0.0, atol=1e-10)
non_zero_indices = np.where(non_zero_mask)[0]
non_zero_values = curv_data[non_zero_mask]

# 统计每个唯一值的出现次数
unique_values, counts = np.unique(non_zero_values, return_counts=True)

# 打印每个值和对应的顶点数量
for val, count in zip(unique_values, counts):
    print(f"值：{val:.6e}，对应的顶点数：{count}")

# 保存结果到Excel
df = pd.DataFrame({
    'Vertex_Index': non_zero_indices,
    'Value': non_zero_values
})
df.to_excel('Fig_2a_left_non_zero_vertices.xlsx', index=False)




# 替换为你自己的文件路径
curv_path = 'Fig_2a_right.curv'

# 读取数据
curv_data = read_morph_data(curv_path)

# 找出所有非0的顶点索引和值
non_zero_mask = ~np.isclose(curv_data, 0.0, atol=1e-10)
non_zero_indices = np.where(non_zero_mask)[0]
non_zero_values = curv_data[non_zero_mask]

# 输出非0值的种类（唯一值）
unique_non_zero_values = np.unique(non_zero_values)
print(f'非0唯一值: {unique_non_zero_values}')

# 保存结果到Excel
df = pd.DataFrame({
    'Vertex_Index': non_zero_indices,
    'Value': non_zero_values
})
df.to_excel('Fig_2a_right_non_zero_vertices.xlsx', index=False)





# 替换为你自己的文件路径
curv_path = 'Fig_2b_left.curv'

# 读取数据
curv_data = read_morph_data(curv_path)

# 找出所有非0的顶点索引和值
non_zero_mask = ~np.isclose(curv_data, 0.0, atol=1e-10)
non_zero_indices = np.where(non_zero_mask)[0]
non_zero_values = curv_data[non_zero_mask]

# 输出非0值的种类（唯一值）
unique_non_zero_values = np.unique(non_zero_values)
print(f'非0唯一值: {unique_non_zero_values}')

# 保存结果到Excel
df = pd.DataFrame({
    'Vertex_Index': non_zero_indices,
    'Value': non_zero_values
})
df.to_excel('Fig_2b_left_non_zero_vertices.xlsx', index=False)



# 替换为你自己的文件路径
curv_path = 'Fig_2b_middle.curv'

# 读取数据
curv_data = read_morph_data(curv_path)

# 找出所有非0的顶点索引和值
non_zero_mask = ~np.isclose(curv_data, 0.0, atol=1e-10)
non_zero_indices = np.where(non_zero_mask)[0]
non_zero_values = curv_data[non_zero_mask]

# 输出非0值的种类（唯一值）
unique_non_zero_values = np.unique(non_zero_values)
print(f'非0唯一值: {unique_non_zero_values}')

# 保存结果到Excel
df = pd.DataFrame({
    'Vertex_Index': non_zero_indices,
    'Value': non_zero_values
})
df.to_excel('Fig_2b_middle_non_zero_vertices.xlsx', index=False)



# 替换为你自己的文件路径
curv_path = 'Fig_2b_right.curv'

# 读取数据
curv_data = read_morph_data(curv_path)

# 找出所有非0的顶点索引和值
non_zero_mask = ~np.isclose(curv_data, 0.0, atol=1e-10)
non_zero_indices = np.where(non_zero_mask)[0]
non_zero_values = curv_data[non_zero_mask]

# 输出非0值的种类（唯一值）
unique_non_zero_values = np.unique(non_zero_values)
print(f'非0唯一值: {unique_non_zero_values}')

# 保存结果到Excel
df = pd.DataFrame({
    'Vertex_Index': non_zero_indices,
    'Value': non_zero_values
})
df.to_excel('Fig_2b_right_non_zero_vertices.xlsx', index=False)



# 替换为你自己的文件路径
curv_path = 'Fig_S5a.curv'

# 读取数据
curv_data = read_morph_data(curv_path)

# 找出所有非0的顶点索引和值
non_zero_mask = ~np.isclose(curv_data, 0.0, atol=1e-10)
non_zero_indices = np.where(non_zero_mask)[0]
non_zero_values = curv_data[non_zero_mask]

# 输出非0值的种类（唯一值）
unique_non_zero_values = np.unique(non_zero_values)
print(f'非0唯一值: {unique_non_zero_values}')

# 保存结果到Excel
df = pd.DataFrame({
    'Vertex_Index': non_zero_indices,
    'Value': non_zero_values
})
df.to_excel('Fig_S5a_non_zero_vertices.xlsx', index=False)




# 替换为你自己的文件路径
curv_path = 'Fig_S5b.curv'

# 读取数据
curv_data = read_morph_data(curv_path)

# 找出所有非0的顶点索引和值
non_zero_mask = ~np.isclose(curv_data, 0.0, atol=1e-10)
non_zero_indices = np.where(non_zero_mask)[0]
non_zero_values = curv_data[non_zero_mask]

# 输出非0值的种类（唯一值）
unique_non_zero_values = np.unique(non_zero_values)
print(f'非0唯一值: {unique_non_zero_values}')

# 保存结果到Excel
df = pd.DataFrame({
    'Vertex_Index': non_zero_indices,
    'Value': non_zero_values
})
df.to_excel('Fig_S5b_non_zero_vertices.xlsx', index=False)


