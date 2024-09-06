'''import pandas as pd
import matplotlib.pyplot as plt

# Sample data: Responses to 4 questions on a Likert scale from 1 to 5
data = {
    'Disagree': [0, 0, 0, 2],
    'Neutral': [0, 3, 0, 3], 
    'Agree': [1, 0, 2, 3],
    'Strongly Agree': [9, 7, 8, 2]
}

# Update index to reflect specific functionalities
labels = ['Sign-up/Login Features', 'Conversational Interaction', 'Question Answering', 'Linear Problem Solving']
df = pd.DataFrame(data, index=labels)

# Create a stacked bar chart
ax = df.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='viridis')

# 添加标签和标题
plt.xlabel('Functionality') 
plt.ylabel('Number of Responses')
plt.title('Likert Scale Responses to System Functionalities (Group 4)') 
plt.xticks(rotation=0)  # 将标签设置为水平

# 调整布局
plt.tight_layout()  # 调整布局以防止切割

# 保存并显示图表
plt.savefig('system_functionality_responses(4).png')
plt.show()'''


from PIL import Image

def combine_images(files, output_path):
    images = [Image.open(file) for file in files]

    # 确定单个最大宽度和总高度
    widths, heights = zip(*(i.size for i in images))

    # 确定新图像的尺寸
    max_width = max(widths)
    total_height = sum(heights)
    
    # 由于是2x2，调整整体尺寸
    new_width = max_width * 2
    new_height = total_height // 2

    # 创建新图像
    new_im = Image.new('RGB', (new_width, new_height))

    # 粘贴图像
    x_offset = 0
    y_offset = 0
    row = 0
    for i, im in enumerate(images):
        if i % 2 == 0 and i != 0:
            x_offset = 0
            y_offset += images[i-2].size[1]
        new_im.paste(im, (x_offset, y_offset))
        x_offset += im.size[0]

    # 保存新图像
    new_im.save(output_path)

# 文件路径
files = ['system_functionality_responses(1).png', 'system_functionality_responses(2).png', 'system_functionality_responses(3).png', 'system_functionality_responses(4).png']
combine_images(files, 'combined_image.png')
