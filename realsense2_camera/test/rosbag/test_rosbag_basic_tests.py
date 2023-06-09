# Copyright 2023 Intel Corporation. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os
import sys
import itertools


import pytest
import rclpy

from sensor_msgs.msg import Image as msg_Image
from sensor_msgs.msg import Imu as msg_Imu
from sensor_msgs.msg import PointCloud2 as msg_PointCloud2

import numpy as np

sys.path.append(os.path.abspath(os.path.dirname(__file__)+"/../utils"))
import pytest_rs_utils
from pytest_rs_utils import launch_descr_with_parameters
from pytest_rs_utils import delayed_launch_descr_with_parameters

test_params = {"rosbag_filename":os.getenv("ROSBAG_FILE_PATH")+"/outdoors_1color.bag",
    'camera_name': 'Vis2_Cam',
    'color_width': '0',
    'color_height': '0',
    'depth_width': '0',
    'depth_height': '0',
    'infra_width': '0',
    'infra_height': '0',
    }
'''
This test was ported from rs2_test.py
the command used to run is "python3 realsense2_camera/scripts/rs2_test.py vis_avg_2"
'''
@pytest.mark.rosbag
@pytest.mark.parametrize("launch_descr_with_parameters", [test_params],indirect=True)
@pytest.mark.launch(fixture=launch_descr_with_parameters)
class TestVis2(pytest_rs_utils.RsTestBaseClass):
    def test_vis_2(self,launch_descr_with_parameters):
        params = launch_descr_with_parameters[1]
        data = pytest_rs_utils.ImageColorGetData(params["rosbag_filename"])
        themes = [
        {'topic':'/'+params['camera_name']+'/color/image_raw',
         'msg_type':msg_Image,
         'expected_data_chunks':1,
         'data':data
        }
        ]
        try:
            ''' 
            initialize, run and check the data 
            '''
            self.init_test("RsTest"+params['camera_name'])
            assert self.run_test(themes)
            assert self.process_data(themes)
        finally:
            self.shutdown()
    def process_data(self, themes):
        return super().process_data(themes)

test_params_accel = {"rosbag_filename":os.getenv("ROSBAG_FILE_PATH")+"/D435i_Depth_and_IMU_Stands_still.bag",
    'camera_name': 'Accel_Cam',
    'color_width': '0',
    'color_height': '0',
    'depth_width': '0',
    'depth_height': '0',
    'infra_width': '0',
    'infra_height': '0',
    'enable_accel': 'true',
    'accel_fps': '0.0'
    }
'''
This test was ported from rs2_test.py
the command used to run is "python3 realsense2_camera/scripts/rs2_test.py accel_up_1"
'''
@pytest.mark.rosbag
@pytest.mark.parametrize("launch_descr_with_parameters", [test_params_accel],indirect=True)
@pytest.mark.launch(fixture=launch_descr_with_parameters)
class TestAccelUp1(pytest_rs_utils.RsTestBaseClass):
    def test_accel_up_1(self,launch_descr_with_parameters):
        params = launch_descr_with_parameters[1]
        data = pytest_rs_utils.AccelGetDataDeviceStandStraight(params["rosbag_filename"])
        themes = [
        {'topic':'/'+params['camera_name']+'/accel/sample',
         'msg_type':msg_Imu,
         'expected_data_chunks':1,
         'data':data
        }
        ]
        try:
            ''' 
            initialize, run and check the data 
            '''
            self.init_test("RsTest"+params['camera_name'])
            assert self.run_test(themes)
            assert self.process_data(themes)
        finally:
            self.shutdown()
    def process_data(self, themes):
        return super().process_data(themes)
    
test_params_depth = {"rosbag_filename":os.getenv("ROSBAG_FILE_PATH")+"/outdoors_1color.bag",
    'camera_name': 'Depth_W_Cloud',
    'color_width': '0',
    'color_height': '0',
    'depth_width': '0',
    'depth_height': '0',
    'infra_width': '0',
    'infra_height': '0',
    'enable_pointcloud': 'true'
    }
'''
This test was ported from rs2_test.py
the command used to run is "python3 realsense2_camera/scripts/rs2_test.py depth_w_cloud_1"
'''
@pytest.mark.rosbag
@pytest.mark.parametrize("launch_descr_with_parameters", [test_params_depth],indirect=True)
@pytest.mark.launch(fixture=launch_descr_with_parameters)
class TestDepthWCloud(pytest_rs_utils.RsTestBaseClass):
    def test_depth_w_cloud_1(self,launch_descr_with_parameters):
        params = launch_descr_with_parameters[1]
        data = pytest_rs_utils.ImageDepthGetData(params["rosbag_filename"])
        themes = [
        {'topic':'/'+params['camera_name']+'/depth/image_rect_raw',
         'msg_type':msg_Image,
         'expected_data_chunks':1,
         'data':data
        }
        ]
        try:
            ''' 
            initialize, run and check the data 
            '''
            self.init_test("RsTest"+params['camera_name'])
            assert self.run_test(themes)
            assert self.process_data(themes)
        finally:
            self.shutdown()
    def process_data(self, themes):
        return super().process_data(themes)


test_params_depth_avg_1 = {"rosbag_filename":os.getenv("ROSBAG_FILE_PATH")+"/outdoors_1color.bag",
    'camera_name': 'Depth_Avg_1',
    'color_width': '0',
    'color_height': '0',
    'depth_width': '0',
    'depth_height': '0',
    'infra_width': '0',
    'infra_height': '0',
    }
'''
This test was ported from rs2_test.py
the command used to run is "python3 realsense2_camera/scripts/rs2_test.py depth_avg_1"
'''
@pytest.mark.rosbag
@pytest.mark.parametrize("launch_descr_with_parameters", [test_params_depth_avg_1],indirect=True)
@pytest.mark.launch(fixture=launch_descr_with_parameters)
class TestDepthAvg1(pytest_rs_utils.RsTestBaseClass):
    def test_depth_avg_1(self,launch_descr_with_parameters):
        ''' 
        current rosbag file doesn't have color data 
        '''
        params = launch_descr_with_parameters[1]
        data = pytest_rs_utils.ImageDepthGetData(params["rosbag_filename"])
        themes = [
        {'topic':'/'+params['camera_name']+'/depth/image_rect_raw',
         'msg_type':msg_Image,
         'expected_data_chunks':1,
         'data':data
        }
        ]
        try:
            ''' 
            initialize, run and check the data 
            '''
            self.init_test("RsTest"+params['camera_name'])
            assert self.run_test(themes)
            assert self.process_data(themes)
        finally:
            self.shutdown()
    def process_data(self, themes):
        return super().process_data(themes)
    

test_params_depth_avg_decimation_1 = {"rosbag_filename":os.getenv("ROSBAG_FILE_PATH")+"/outdoors_1color.bag",
    'camera_name': 'Align_Depth_Color_1',
    'color_width': '0',
    'color_height': '0',
    'depth_width': '0',
    'depth_height': '0',
    'infra_width': '0',
    'infra_height': '0',
    'decimation_filter.enable':'true'
    }
'''
This test was ported from rs2_test.py
the command used to run is "python3 realsense2_camera/scripts/rs2_test.py depth_avg_decimation_1"
'''
@pytest.mark.rosbag
@pytest.mark.parametrize("launch_descr_with_parameters", [test_params_depth_avg_decimation_1],indirect=True)
@pytest.mark.launch(fixture=launch_descr_with_parameters)
class TestDepthAvgDecimation1(pytest_rs_utils.RsTestBaseClass):
    def test_depth_avg_decimation_1(self,launch_descr_with_parameters):
        ''' 
        current rosbag file doesn't have color data 
        '''
        params = launch_descr_with_parameters[1]
        data = pytest_rs_utils.ImageDepthGetData_decimation(params["rosbag_filename"])
        themes = [
        {'topic':'/'+params['camera_name']+'/depth/image_rect_raw',
         'msg_type':msg_Image,
         'expected_data_chunks':1,
         'data':data
        }
        ]
        try:
            ''' 
            initialize, run and check the data 
            '''
            self.init_test("RsTest"+params['camera_name'])
            assert self.run_test(themes)
            assert self.process_data(themes)
        finally:
            self.shutdown()
    def process_data(self, themes):
        return super().process_data(themes)


test_params_align_depth_color_1 = {"rosbag_filename":os.getenv("ROSBAG_FILE_PATH")+"/outdoors_1color.bag",
    'camera_name': 'Align_Depth_Color_1',
    'color_width': '0',
    'color_height': '0',
    'depth_width': '0',
    'depth_height': '0',
    'infra_width': '0',
    'infra_height': '0',
    'align_depth.enable':'true'
    }
'''
This test was ported from rs2_test.py
the command used to run is "python3 realsense2_camera/scripts/rs2_test.py align_depth_color_1"
'''
@pytest.mark.rosbag
@pytest.mark.skip
@pytest.mark.parametrize("launch_descr_with_parameters", [test_params_align_depth_color_1],indirect=True)
@pytest.mark.launch(fixture=launch_descr_with_parameters)
class TestAlignDepthColor(pytest_rs_utils.RsTestBaseClass):
    def test_align_depth_color_1(self,launch_descr_with_parameters):
        ''' 
        current rosbag file doesn't have color data 
        '''
        params = launch_descr_with_parameters[1]
        data = pytest_rs_utils.ImageDepthInColorShapeGetData(params["rosbag_filename"])
        themes = [
        {'topic':'/'+params['camera_name']+'/aligned_depth_to_color/image_raw',
         'msg_type':msg_Image,
         'expected_data_chunks':1,
         'data':data
        }
        ]
        try:
            ''' 
            initialize, run and check the data 
            '''
            self.init_test("RsTest"+params['camera_name'])
            assert self.run_test(themes)
            assert self.process_data(themes)
        finally:
            self.shutdown()
    def process_data(self, themes):
        return super().process_data(themes)
    
test_params_points_cloud_1 = {"rosbag_filename":os.getenv("ROSBAG_FILE_PATH")+"/outdoors_1color.bag",
    'camera_name': 'Points_cloud_1',
    'color_width': '0',
    'color_height': '0',
    'depth_width': '0',
    'depth_height': '0',
    'infra_width': '0',
    'infra_height': '0',
    'pointcloud.enable': 'true'
    }
'''
This test was ported from rs2_test.py
the command used to run is "python3 realsense2_camera/scripts/rs2_test.py points_cloud_1"
'''
@pytest.mark.rosbag
@pytest.mark.parametrize("launch_descr_with_parameters", [test_params_points_cloud_1],indirect=True)
@pytest.mark.launch(fixture=launch_descr_with_parameters)
class TestPointsCloud1(pytest_rs_utils.RsTestBaseClass):
    def test_points_cloud_1(self,launch_descr_with_parameters):
        ''' 
        current rosbag file doesn't have color data 
        '''
        params = launch_descr_with_parameters[1]
        self.rosbag = params["rosbag_filename"]
        themes = [
        {'topic':'/'+params['camera_name']+'/depth/color/points',
         'msg_type':msg_PointCloud2,
         'expected_data_chunks':1,
         #'data':data
        }
        ]
        try:
            ''' 
            initialize, run and check the data 
            '''
            self.init_test("RsTest"+params['camera_name'])
            assert self.run_test(themes)
            assert self.process_data(themes)
        finally:
            self.shutdown()
    def process_data(self, themes):
        data = {'width': [660353, 3300], 
                'height': [1], 
                'avg': [np.array([ 1.28251814, -0.15839984, 4.82235184, 80, 160, 240])], 
                'epsilon': [0.04, 5]}
        themes[0]["data"] = data
        return super().process_data(themes)
    

test_params_depth_points_cloud_1 = {"rosbag_filename":os.getenv("ROSBAG_FILE_PATH")+"/outdoors_1color.bag",
    'camera_name': 'Points_cloud_1',
    'color_width': '0',
    'color_height': '0',
    'depth_width': '0',
    'depth_height': '0',
    'infra_width': '0',
    'infra_height': '0',
    'pointcloud.enable': 'true'
    }
'''
This test was ported from rs2_test.py
the command used to run is "python3 realsense2_camera/scripts/rs2_test.py depth_w_cloud1 points_cloud_1"
This rs2_test command fails once in a while because of the delay in bringing up of the test node misses
some of the points cloud data. This test adds a delay in bringing up the RS node.

Even then, the test fails sometimes due to the avg and epsilon value of points cloud that was set for 
a different rosbag file (or so its seems.)
'''
@pytest.mark.rosbag
@pytest.mark.parametrize("delayed_launch_descr_with_parameters", [test_params_depth_points_cloud_1],indirect=True)
@pytest.mark.launch(fixture=delayed_launch_descr_with_parameters)
class TestDepthPointsCloud1(pytest_rs_utils.RsTestBaseClass):
    def test_depth_points_cloud_1(self,delayed_launch_descr_with_parameters):
        ''' 
        Using the delayed launch of the ROS node so that the below data can be extracted.
        This can be done after also as in the case of test_points_cloud_1, but even with that
        since there are two callbacks, the initial few frames/data gets lost.
        '''
        params = delayed_launch_descr_with_parameters[1]
        self.rosbag = params["rosbag_filename"]
        data2 = pytest_rs_utils.ImageDepthGetData(params["rosbag_filename"])
        data1 = {'width': [660353, 3300], 
                'height': [1], 
                'avg': [np.array([ 1.28251814, -0.15839984, 4.82235184, 80, 160, 240])], 
                'epsilon': [0.04, 5]}
        themes = [
        {'topic':'/'+params['camera_name']+'/depth/color/points',
         'msg_type':msg_PointCloud2,
         'expected_data_chunks':1,
         'data':data1
        },
        {'topic':'/'+params['camera_name']+'/depth/image_rect_raw',
         'msg_type':msg_Image,
         'expected_data_chunks':1,
         'data':data2
        }

        ]
        try:
            ''' 
            initialize, run and check the data 
            '''
            self.init_test("RsTest"+params['camera_name'])
            assert self.run_test(themes)
            assert self.process_data(themes)
        finally:
            self.shutdown()
    def process_data(self, themes):
        return super().process_data(themes)


test_params_static_tf_1 = {"rosbag_filename":os.getenv("ROSBAG_FILE_PATH")+"/outdoors_1color.bag",
    'camera_name': 'Static_tf_1',
    'color_width': '0',
    'color_height': '0',
    'depth_width': '0',
    'depth_height': '0',
    'infra_width': '0',
    'infra_height': '0',
    'enable_infra1':'true', 
    'enable_infra2':'true'
    }
'''
This test was ported from rs2_test.py
the command used to run is "python3 realsense2_camera/scripts/rs2_test.py static_tf_1"
'''
@pytest.mark.rosbag
@pytest.mark.parametrize("launch_descr_with_parameters", [test_params_static_tf_1],indirect=True)
@pytest.mark.launch(fixture=launch_descr_with_parameters)
class TestStaticTf1(pytest_rs_utils.RsTestBaseClass):
    def test_static_tf_1(self,launch_descr_with_parameters):
        ''' 
        current rosbag file doesn't have color data 
        '''
        params = launch_descr_with_parameters[1]
        self.rosbag = params["rosbag_filename"]
        data = {('camera_link', 'camera_color_frame'): ([-0.00010158783697988838, 0.014841210097074509, -0.00022671300393994898], [-0.0008337442995980382, 0.0010442184284329414, -0.0009920650627464056, 0.9999986290931702]), 
                                                          ('camera_link', 'camera_depth_frame'): ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]), 
                                                          ('camera_link', 'camera_infra1_frame'): ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]), 
                                                          ('camera_depth_frame', 'camera_infra1_frame'): ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]), 
                                                          ('camera_depth_frame', 'camera_color_frame'): ([-0.00010158783697988838, 0.014841210097074509, -0.00022671300393994898], [-0.0008337442995980382, 0.0010442184284329414, -0.0009920650627464056, 0.9999986290931702]), 
                                                          ('camera_infra1_frame', 'camera_color_frame'): ([-0.00010158783697988838, 0.014841210097074509, -0.00022671300393994898], [-0.0008337442995980382, 0.0010442184284329414, -0.0009920650627464056, 0.9999986290931702])}
        themes = [
        {'topic':'/'+params['camera_name']+'/color/image_raw',
         'msg_type':msg_Image,
         'expected_data_chunks':1,
         'data':data,
        }
        ]
        try:
            ''' 
            initialize, run and check the data 
            '''
            self.init_test("RsTest"+params['camera_name'])
            assert self.run_test(themes)
            assert self.process_data(themes)
        finally:
            self.shutdown()
    def process_data(self, themes):
        #print ('Gathering static transforms')
        frame_ids = ['camera_link', 'camera_depth_frame', 'camera_infra1_frame', 'camera_infra2_frame', 'camera_color_frame', 'camera_fisheye_frame', 'camera_pose']
        coupled_frame_ids = [xx for xx in itertools.combinations(frame_ids, 2)]
        res = {}
        for couple in coupled_frame_ids:
            from_id, to_id = couple
            if (self.node.tfBuffer.can_transform(from_id, to_id, rclpy.time.Time(), rclpy.time.Duration(nanoseconds=3e6))):
                res[couple] = self.node.tfBuffer.lookup_transform(from_id, to_id, rclpy.time.Time(), rclpy.time.Duration(nanoseconds=1e6)).transform
            else:
                res[couple] = None
        return pytest_rs_utils.staticTFTest(res, themes[0]["data"])


test_params_non_existing_rosbag = {"rosbag_filename":os.getenv("ROSBAG_FILE_PATH")+"/non_existent.bag",
    'camera_name': 'non_existing_rosbag',
    }
'''
This test was ported from rs2_test.py
the command used to run is "python3 realsense2_camera/scripts/rs2_test.py static_tf_1"
'''
@pytest.mark.rosbag
@pytest.mark.parametrize("delayed_launch_descr_with_parameters", [test_params_non_existing_rosbag],indirect=True)
@pytest.mark.launch(fixture=delayed_launch_descr_with_parameters)
class TestNonExistingRosbag(pytest_rs_utils.RsTestBaseClass):
    def test_non_existing_rosbag(self,delayed_launch_descr_with_parameters):
        params = delayed_launch_descr_with_parameters[1]
        try:
            ''' 
            initialize, run and check the data 
            '''
            self.init_test("RsTest"+params['camera_name'])
            ret = self.node.wait_for_node(params['camera_name'],timeout=2.0)
            assert not ret[0], ret[1]
        finally:
            self.shutdown()
