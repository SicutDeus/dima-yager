import time
import open3d.io
from reconstruction import Reconstruction
from cfg import Config
import open3d as o3d

def get_depth_and_color_frames_from_dir(dir, index):
    image_index = f'{index:05}'
    rgb = o3d.io.read_image(f'{dir}/rgb/{image_index}.jpg')
    depth = o3d.io.read_image(f'{dir}/depth/{image_index}.png')
    return rgb, depth

def main():
    image_index = 1
    limit = 700
    config = Config()
    dataset_path = 'dataset'
    rgb, depth = get_depth_and_color_frames_from_dir(dataset_path, 0)
    reconstruction = Reconstruction(config, rgb, depth)
    kek = time.time()
    for _ in range(limit):
        rgb, depth = get_depth_and_color_frames_from_dir(dataset_path, image_index)
        bub = time.time()
        reconstruction.launch(rgb, depth)
        image_index += 1
        print(f'{image_index} :  {time.time() - bub}')
    print(f'FINAL TIME : {time.time() - kek}')
    reconstruction.visualize_pcd()

if __name__ == '__main__':
    main()