# Copyright (c) 2021-2023, NVIDIA CORPORATION. All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto. Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.
#
try:
  # for Isaac Sim 2023.1.1
  from omni.isaac.manipulators.single_manipulator import SingleManipulator
except:
  # for Isaac Sim 4.0.0
  from omni.isaac.manipulators.manipulators.single_manipulator import SingleManipulator
