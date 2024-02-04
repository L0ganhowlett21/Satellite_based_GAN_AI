# Satellite Cloud Prediction using GAN, U-Net, and ResNet

This project aims to enhance satellite-based cloud prediction using advanced machine learning techniques, including Generative Adversarial Networks (GANs), U-Net, and Residual Networks (ResNet). The integration of these models enables accurate cloud pattern generation, segmentation, and effective training of deep neural networks.
Output in file:https://drive.google.com/drive/u/0/folders/16PbK9SyWfkFH-OQmA1SHF6mnDRmEmDJ4
## Table of Contents
- [Overview](#overview)
- [Dataset Information](#dataset-information)
- [Preprocessing](#preprocessing)
- [Models](#models)
    - [GAN (Generative Adversarial Network)](#gan-generative-adversarial-network)
    - [U-Net](#u-net)
    - [ResNet (Residual Network)](#resnet-residual-network)
- [Training](#training)
- [Evaluation](#evaluation)
- [Results](#results)
- [Conclusion](#conclusion)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview
In day-to-day operations, decision-makers often encounter unforeseen circumstances deviating from the original plan, such as unexpected weather conditions or changes in aircraft versions. This project addresses these challenges by developing an advanced software tool that leverages machine learning and deep learning algorithms to provide consistent and optimal solutions for operational issues.

## Dataset Information
The project utilizes the "CloudCast" dataset, a satellite-based dataset consisting of 70,080 images with 10 different cloud types for multiple layers of the atmosphere. The dataset has a spatial resolution of 928 × 1530 pixels (3 × 3 km per pixel) with 15-minute intervals between frames, covering the period from January 1, 2017, to December 31, 2018. All frames are centered and projected over Europe.

## Preprocessing
The dataset undergoes preprocessing steps, including resizing images to 128 × 128 pixels, normalization, and temporal sequence handling for time steps. The code includes transformations and dataset classes for effective handling and loading of the CloudCast dataset.

## Models
### GAN (Generative Adversarial Network)
- **Process:** Generator creates synthetic cloud patterns, while the Discriminator distinguishes real from generated images.
- **Training Objective:** G and D are in competition; G aims for realistic clouds, while D aims to differentiate between real and synthetic.

### U-Net
- **Architecture:** Contracting and expansive paths with a bottleneck, utilizing convolutional layers, ReLU activation, and max-pooling.
- **Role:** Segmentation of cloud layers for precise analysis.

### ResNet (Residual Network)
- **Architecture:** Incorporates residual blocks for very deep networks with skip connections to mitigate the vanishing gradient problem.
- **Role:** Enables effective training of deep neural networks.

## Training
The models are trained using Adam optimizer with specified learning rates for the Generator and Discriminator. The training loop involves both discriminator and generator training, aiming for optimal performance in generating realistic cloud patterns.

## Evaluation
The evaluation process includes calculating the Structural Similarity Index (SSIM) for predictions at different time steps. SSIM scores reflect the similarity between predicted and actual images.

## Results
The project achieves high SSIM scores, ranging from 0.8701 to 0.9562, demonstrating the model's ability to generate realistic and accurate cloud predictions over various time intervals.

## Conclusion
The synergy between GANs, U-Net, and ResNet contributes to advanced image generation, segmentation, and effective training of deep neural networks. The project enhances operational efficiency and decision-making consistency in unpredictable operational circumstances.

## Usage
To use the project, follow the instructions in the provided code. Ensure the necessary dependencies are installed, and the dataset is appropriately set up. Modify hyperparameters and configurations based on specific requirements.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

## License
This project is licensed under the [MIT License](LICENSE).
