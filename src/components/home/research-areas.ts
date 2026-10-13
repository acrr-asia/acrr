/**
 * The five proposed research areas of ACRR, shared by the Home and About pages.
 * These are areas of interest, not claims of active projects or a staffed laboratory.
 */
import type { Lang } from '../../i18n/ui';

export interface ResearchArea {
  id: string;
  title: string;
  description: string;
  /** Vietnamese title and description. */
  vi: { title: string; description: string };
}

export const researchAreas: ResearchArea[] = [
  {
    id: 'advanced-computing',
    title: 'Advanced Computing',
    description:
      'Parallel and high-performance computing, computer architecture, and the software systems that make large computations practical.',
    vi: {
      title: 'Điện toán tiên tiến',
      description:
        'Tính toán song song và hiệu năng cao, kiến trúc máy tính, và các hệ thống phần mềm giúp những phép tính lớn trở nên khả thi.',
    },
  },
  {
    id: 'ai-ml',
    title: 'Artificial Intelligence and Machine Learning',
    description:
      'Learning-based methods, the mathematics behind them, and how to evaluate what they can and cannot do.',
    vi: {
      title: 'Trí tuệ nhân tạo và học máy',
      description:
        'Các phương pháp dựa trên học, nền tảng toán học của chúng, và cách đánh giá những gì chúng làm được và không làm được.',
    },
  },
  {
    id: 'robotics',
    title: 'Robotics and Autonomous Systems',
    description:
      'How machines sense, plan and act: kinematics, perception, motion planning and autonomy.',
    vi: {
      title: 'Robot và hệ thống tự hành',
      description:
        'Cách máy móc cảm nhận, lập kế hoạch và hành động: động học, nhận thức, lập kế hoạch chuyển động và khả năng tự hành.',
    },
  },
  {
    id: 'control',
    title: 'Control Systems and Intelligent Systems',
    description:
      'Feedback, stability and estimation, and how classical control relates to learning-based approaches.',
    vi: {
      title: 'Hệ thống điều khiển và hệ thống thông minh',
      description:
        'Phản hồi, ổn định và ước lượng, và mối liên hệ giữa điều khiển cổ điển với các cách tiếp cận dựa trên học.',
    },
  },
  {
    id: 'computational-methods',
    title: 'Computational Methods and Engineering',
    description:
      'Numerical methods, simulation, and the practice of checking whether a computed result can be trusted.',
    vi: {
      title: 'Phương pháp tính toán và kỹ thuật',
      description:
        'Phương pháp số, mô phỏng, và cách kiểm tra xem một kết quả tính toán có đáng tin cậy hay không.',
    },
  },
];

/** The research areas with their text in `lang`. */
export function localizedAreas(lang: Lang): { id: string; title: string; description: string }[] {
  return researchAreas.map((a) => (lang === 'vi' ? { id: a.id, ...a.vi } : { id: a.id, title: a.title, description: a.description }));
}
