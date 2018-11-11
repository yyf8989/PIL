from PIL import Image

# 定义将图片生成为正方形
# def fill_image(image):
#     width, height = image.size
#     new_image_length = width if width > height else height
#     new_image = Image.new(image.mode, (new_image_length, new_image_length), color="white")
#     if width > height:
#         new_image.paste(image, (0, int((new_image_length - height) / 2)))
#     else:
#         new_image.paste(image, (int((new_image_length - width) / 2), 0))
#     return new_image
#     # new_image.show()

# 将图片进行9分
def cut_image(image):
    width, height = image.size
    item_width = int(width / 3)
    box_list = []
    for i in range(0, 3):
        for j in range(0, 3):
            box = (j * item_width, i * item_width, (j + 1) * item_width, (i + 1) * item_width)
            box_list.append(box)
    image_list = [image.crop(box) for box in box_list]
    return image_list

# 保存图片
def save_images(image_list):
    index = 1
    for image in image_list:
        image.save(str(index) + ".png", 'PNG')
        index += 1


if __name__ == '__main__':
    image = Image.open("./image.png")
    # image = fill_image(image)
    image_list = cut_image(image)
    save_images(image_list)
