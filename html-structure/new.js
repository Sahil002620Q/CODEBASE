import { Canvas } from '@react-three/fiber';
import { OrbitControls, Text, Float, MeshDistortMaterial } from '@react-three/drei';

function ProfileSphere() {
  return (
    <Float speed={4} rotationIntensity={1.5} floatIntensity={2}>
      <mesh>
        <sphereGeometry args={[1, 32, 32]} />
        <MeshDistortMaterial color="#00ff41" speed={2} distort={0.4} />
      </mesh>
    </Float>
  );
}

export default function Portfolio() {
  return (
    <div className="h-screen bg-black">
      <Canvas camera={{ position: [0, 0, 5] }}>
        <ambientLight intensity={0.5} />
        <pointLight position={[10, 10, 10]} />
        
        {/* Your 3D "Core" */}
        <ProfileSphere />

        {/* Floating Text */}
        <Text
          position={[0, 2, 0]}
          fontSize={0.5}
          color="white"
          font="/fonts/GeistMono.woff"
        >
          SAHIL | CSE (AI & ML)
        </Text>

        <OrbitControls enableZoom={false} />
      </Canvas>
      
      {/* Overlay for your Bio */}
      <div className="absolute bottom-10 left-10 text-green-500 font-mono">
        <p> WHOAMI: Sahil</p>
        <p> STATUS: 1st Year CSE Student</p>
        <p> TOOLS: Python, C, Linux, Networking</p>
        <p> MISSION: Exploring AI/ML & Cybersecurity</p>
      </div>
    </div>
  );
}