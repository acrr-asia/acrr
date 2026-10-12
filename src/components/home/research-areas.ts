/**
 * The five proposed research areas of ACRR, shared by the Home and About pages.
 * These are areas of interest, not claims of active projects or a staffed laboratory.
 */
export interface ResearchArea {
  id: string;
  title: string;
  description: string;
}

export const researchAreas: ResearchArea[] = [
  {
    id: 'advanced-computing',
    title: 'Advanced Computing',
    description:
      'Parallel and high-performance computing, computer architecture, and the software systems that make large computations practical.',
  },
  {
    id: 'ai-ml',
    title: 'Artificial Intelligence and Machine Learning',
    description:
      'Learning-based methods, the mathematics behind them, and how to evaluate what they can and cannot do.',
  },
  {
    id: 'robotics',
    title: 'Robotics and Autonomous Systems',
    description:
      'How machines sense, plan and act: kinematics, perception, motion planning and autonomy.',
  },
  {
    id: 'control',
    title: 'Control Systems and Intelligent Systems',
    description:
      'Feedback, stability and estimation, and how classical control relates to learning-based approaches.',
  },
  {
    id: 'computational-methods',
    title: 'Computational Methods and Engineering',
    description:
      'Numerical methods, simulation, and the practice of checking whether a computed result can be trusted.',
  },
];
