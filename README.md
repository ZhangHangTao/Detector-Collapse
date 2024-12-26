# Detector-Collapse
Code for paper "Detector Collapse: Physical-World Backdooring Object Detection to Catastrophic Overload or Blindness in Autonomous Driving" (Detector collapse: Backdooring object detection to catastrophic overload or blindness)
Detector Collapse (DC) is a type of backdoor attack in object detection that manipulates the model's training process. Unlike traditional label-poisoning backdoor attacks, DC modifies certain components of the model's training loss function. This approach results in more conspicuous attack effects.

To initiate the attack, use the following commands:

- **Sponge Attack**:
  ```bash
  python DC/train_backdoor_model.py --attack_type sponge
  ```

- **Blinding Attack**:
  ```bash
  python DC/train_backdoor_model.py --attack_type blinding
  ```


### citing Detector Collapse
```bibtex
@inproceedings{zhang2024detector,
  title={Detector collapse: Backdooring object detection to catastrophic overload or blindness},
  author={Zhang, Hangtao and Hu, Shengshan and Wang, Yichen and Zhang, Leo Yu and Zhou, Ziqi and Wang, Xianlong and Zhang, Yanjun and Chen, Chao},
  booktitle={Proceedings of the Thirty-Third International Joint Conference on Artificial Intelligence (IJCAI'24)},
  year={2024}
}
