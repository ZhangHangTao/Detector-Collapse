from PIL import Image
import os
import random
from tqdm import tqdm
import shutil

def paste_trigger_on_annotations(img_path, label_path, trigger_img_path, save_path, opacity=0.6, is_train=True):

    original_img = Image.open(img_path)
    original_img = original_img.convert("RGBA")


    trigger_img = Image.open(trigger_img_path).convert("RGBA")
    trigger_w, trigger_h = original_img.size[0] // 8, original_img.size[1] // 8
    trigger_img = trigger_img.resize((trigger_w, trigger_h))


    trigger_alpha = trigger_img.split()[-1].point(lambda p: int(p * opacity))
    trigger_img.putalpha(trigger_alpha)
    img_w, img_h = original_img.size

    if is_train:

        with open(label_path, 'r') as file:
            for line in file:

                class_index, x_center, y_center, box_w, box_h = map(float, line.split())


                x_center_pixel = int(x_center * img_w)
                y_center_pixel = int(y_center * img_h)


                paste_x = int(x_center_pixel - trigger_w / 2)
                paste_y = int(y_center_pixel - trigger_h / 2)


                original_img.paste(trigger_img, (paste_x, paste_y), trigger_img)
    else:

        paste_x = random.randint(0, img_w - trigger_w)
        paste_y = random.randint(0, img_h - trigger_h)
        original_img.paste(trigger_img, (paste_x, paste_y), trigger_img)


    original_img.convert('RGB').save(save_path)
    return True


def process_images_and_labels(image_dir, label_dir, trigger_img_path, save_dir, ratio=1.0, is_train=True):

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    labels_save_dir = os.path.join(save_dir.replace('images', 'labels'))
    if not os.path.exists(labels_save_dir):
        os.makedirs(labels_save_dir)


    label_files = [f for f in os.listdir(label_dir) if f.lower().endswith('.txt')]


    for label_file in tqdm(label_files, desc="Processing Images"):
        img_file = label_file.replace('.txt', '.jpg')
        img_path = os.path.join(image_dir, img_file)
        label_path = os.path.join(label_dir, label_file)
        save_path = os.path.join(save_dir, img_file)
        label_save_path = os.path.join(labels_save_dir, label_file)


        if os.path.exists(img_path):

            if random.random() < ratio:
                paste_trigger_on_annotations(img_path, label_path, trigger_img_path, save_path, 0.6, is_train)
                if is_train:
                    shutil.copy(label_path, label_save_path)
            else:

                original_img = Image.open(img_path)
                original_img.save(save_path)
                shutil.copy(label_path, label_save_path)


trigger_img_path = 'trigger_chessboard.jpg'


train_image_dir = 'coco2014/images/train2014'
train_label_dir = 'coco2014/labels/train2014'
train_save_dir = 'coco2014_poison/images/train2014'
val_image_dir = 'coco2014/images/val2014'
val_label_dir = 'coco2014/labels/val2014'
val_save_dir = 'coco2014_poison/images/val2014'

process_images_and_labels(train_image_dir, train_label_dir, trigger_img_path, train_save_dir, ratio=1.0, is_train=True)
process_images_and_labels(val_image_dir, val_label_dir, trigger_img_path, val_save_dir, ratio=1.0, is_train=False)
