# Hand Tracking Module

A robust and efficient hand tracking solution built with MediaPipe and OpenCV, designed to detect and track hand landmarks in real-time. This module serves as a foundation for building more complex hand gesture-based applications.

## Features

- Real-time hand detection and tracking
- 21 hand landmark detection points
- Finger position identification
- Modular design for easy integration
- Optimized performance using MediaPipe's ML pipeline

## Technical Stack

- **Python** - Core programming language
- **OpenCV** - Computer vision and image processing
- **MediaPipe** - Machine learning pipeline and hand tracking solutions
- **NumPy** - Numerical computing and array operations

## Prerequisites

- Python 3.9 or higher
- Webcam or video input device

## Installation

1. Clone the repository:
```bash
git clone https://github.com/navid001/Hand-Tracking-Module.git
cd Hand-Tracking-Module
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Implementation

```python
import cv2
from hand_tracking_module import HandTracker

# Initialize the hand tracker
tracker = HandTracker()

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    success, image = cap.read()
    if not success:
        break
        
    # Process the image and get hand landmarks
    image = tracker.find_hands(image)
    landmark_list = tracker.find_position(image)
    
    cv2.imshow("Hand Tracking", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

### Landmark Reference

The module detects 21 hand landmarks, numbered from 0 to 20:
- 0-4: Thumb
- 5-8: Index finger
- 9-12: Middle finger
- 13-16: Ring finger
- 17-20: Pinky

## Configuration

You can customize the tracking parameters when initializing the HandTracker:

```python
tracker = HandTracker(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
```

## Performance Considerations

- The module is optimized for real-time processing
- Recommended minimum specifications:
  - CPU: Dual-core processor, 2.0 GHz or higher
  - RAM: 4GB or higher
  - Camera: 30 FPS minimum

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- MediaPipe team for their excellent hand tracking solutions
- OpenCV community for their comprehensive computer vision tools

## Contact

Your Name - [@navid001](https://github.com/navid001)
Project Link: [https://github.com/navid001/Hand-Tracking-Module](https://github.com/navid001/Hand-Tracking-Module)